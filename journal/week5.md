# Week 5 — DynamoDB and Serverless Caching

This week I worked on aspects related to data modelling and implementation using DynamoDB. I focused on designing a Direct Messaging System using Single Table Design and implementing DynamoDB queries using the same approach. Additionally, I worked on provisioning DynamoDB tables with Provisioned Capacity and utilizing a Global Secondary Index (GSI) with DynamoDB.

To gain a better understanding of non-SQL databases, I watched several videos on YouTube, with a special focus on pk, sk, gsi, and lsi concepts. I also had the chance to write utility scripts to facilitate the setup and teardown and debug of DynamoDB data, and I used DynamoDB Local to speed up the data modelling process.

Although I found the coding aspect of the project relatively easier, I had to work hard to understand the modelling conceptually. Despite this, I managed to help other students in the forum to ensure that everyone made it through the week.
Overall, I found this project to be challenging, but it was a great opportunity to learn more about data modelling and implementation using DynamoDB. This week we did not had the chance to do serverless caching, it focused on dynamoDB only. 

Sample conversation data working: 

<img width="1758" alt="Screenshot 2023-03-23 at 23 57 52" src="https://user-images.githubusercontent.com/17580456/227725618-f9097950-3a37-4fc9-99e2-a2cc1b48a57e.png">

Posting messages working: 
<img width="1758" alt="Screenshot 2023-03-25 at 00 14 22" src="https://user-images.githubusercontent.com/17580456/227725631-2034b8be-cbe1-492f-9486-cd89067fc618.png">

New conversation access pattern working:
<img width="1758" alt="Screenshot 2023-03-24 at 23 16 06" src="https://user-images.githubusercontent.com/17580456/227725649-e3ff6dc3-f235-4605-bb51-cfd11b18b658.png">

Posting messages to new conversation:

<img width="1758" alt="Screenshot 2023-03-24 at 23 21 19" src="https://user-images.githubusercontent.com/17580456/227725656-a3cd0a35-b20e-440b-aa26-dc80d82f75c1.png">

Update left working (lambda working): 
<img width="1758" alt="Screenshot 2023-03-25 at 00 17 30" src="https://user-images.githubusercontent.com/17580456/227725634-c0c6d799-9cbb-47d9-b872-1ca6ab40f606.png">
<img width="1758" alt="Screenshot 2023-03-25 at 00 17 39" src="https://user-images.githubusercontent.com/17580456/227725638-91b88a43-e655-489f-b216-3be16748f197.png">

--- bits of code (original, see adapted ones in the repo!) ----- 

## DynamoDB Bash Scripts

```sh
./bin/ddb/schem-load
```


## The Boundaries of DynamoDB

- When you write a query you have provide a Primary Key (equality) eg. pk = 'andrew'
- Are you allowed to "update" the Hash and Range?
  - No, whenever you change a key (simple or composite) eg. pk or sk you have to create a new item.
    - you have to delete the old one
- Key condition expressions for query only for RANGE, HASH is only equality 
- Don't create UUID for entity if you don't have an access pattern for it


3 Access Patterns

## Pattern A  (showing a single conversation)

A user wants to see a list of messages that belong to a message group
The messages must be ordered by the created_at timestamp from newest to oldest (DESC)

```sql
SELECT
  messages.uuid,
  messages.display_name,
  messages.message,
  messages.handle,
  messages.created_at -- sk
FROM messages
WHERE
  messages.message_group_uuid = {{message_group_uuid}} -- pk
ORDER BY messages.created_at DESC
```

> message_group_uuid comes from Pattern B

## Pattern B (list of conversation)

A user wants to see a list of previous conversations.
These conversations are listed from newest to oldest (DESC)
We want to see the other person we are talking to.
We want to see the last message (from whomever) in summary.

```sql
SELECT
  message_groups.uuid,
  message_groups.other_user_uuid,
  message_groups.other_user_display_name,
  message_groups.other_user_handle,
  message_groups.last_message,
  message_groups.last_message_at
FROM message_groups
WHERE
  message_groups.user_uuid = {{user_uuid}} --pk
ORDER BY message_groups.last_message_at DESC
```

> We need a Global Secondary Index (GSI)

## Pattern C (create a message)

```sql
INSERT INTO messages (
  user_uuid,
  display_name,
  handle,
  creaed_at
)
VALUES (
  {{user_uuid}},
  {{display_name}},
  {{handle}},
  {{created_at}}
);
```

## Pattern D (update a message_group for the last message)

When a user creates a message we need to update the conversation
to display the last message information for the conversation

```sql
UPDATE message_groups
SET 
  other_user_uuid = {{other_user_uuid}}
  other_user_display_name = {{other_user_display_name}}
  other_user_handle = {{other_user_handle}}
  last_message = {{last_message}}
  last_message_at = {{last_message_at}}
WHERE 
  message_groups.uuid = {{message_group_uuid}}
  AND message_groups.user_uuid = {{user_uuid}}
```


## Serverless Caching

### Install Momento CLI tool

In your gitpod.yml file add:

```yml
  - name: momento
    before: |
      brew tap momentohq/tap
      brew install momento-cli
```

### Login to Momento

There is no `login` you just have to generate an access token and not lose it. 
 
You cannot rotate out your access token on an existing cache.

If you lost your cache or your cache was comprised you just have to wait for the TTL to expire.

> It might be possible to rotate out the key by specifcing the same cache name and email.

 ```sh
 momento account signup aws --email andrew@exampro.co --region us-east-1
 ```

### Create Cache

```sh
export MOMENTO_AUTH_TOKEN=""
export MOMENTO_TTL_SECONDS="600"
export MOMENTO_CACHE_NAME="cruddur"
gp env MOMENTO_AUTH_TOKEN=""
gp env MOMENTO_TTL_SECONDS="600"
gp env MOMENTO_CACHE_NAME="cruddur"
```

> you might need to do `momento configure` since it might not pick up the env var in the CLI.

Create the cache:

```sh
momento cache create --name cruddur
```


### DynamoDB Stream trigger to update message groups

- create a VPC endpoint for dynamoDB service on your VPC
- create a Python lambda function in your vpc
- enable streams on the table with 'new image' attributes included
- add your function as a trigger on the stream
- grant the lambda IAM role permission to read the DynamoDB stream events

`AWSLambdaInvocation-DynamoDB`

- grant the lambda IAM role permission to update table items


**The Function**

```.py
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(
 'dynamodb',
 region_name='ca-central-1',
 endpoint_url="http://dynamodb.ca-central-1.amazonaws.com"
)

def lambda_handler(event, context):
  pk = event['Records'][0]['dynamodb']['Keys']['pk']['S']
  sk = event['Records'][0]['dynamodb']['Keys']['sk']['S']
  if pk.startswith('MSG#'):
    group_uuid = pk.replace("MSG#","")
    message = event['Records'][0]['dynamodb']['NewImage']['message']['S']
    print("GRUP ===>",group_uuid,message)
    
    table_name = 'cruddur-messages'
    index_name = 'message-group-sk-index'
    table = dynamodb.Table(table_name)
    data = table.query(
      IndexName=index_name,
      KeyConditionExpression=Key('message_group_uuid').eq(group_uuid)
    )
    print("RESP ===>",data['Items'])
    
    # recreate the message group rows with new SK value
    for i in data['Items']:
      delete_item = table.delete_item(Key={'pk': i['pk'], 'sk': i['sk']})
      print("DELETE ===>",delete_item)
      
      response = table.put_item(
        Item={
          'pk': i['pk'],
          'sk': sk,
          'message_group_uuid':i['message_group_uuid'],
          'message':message,
          'user_display_name': i['user_display_name'],
          'user_handle': i['user_handle'],
          'user_uuid': i['user_uuid']
        }
      )
      print("CREATE ===>",response)
```
