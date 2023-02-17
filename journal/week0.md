# Week 0 — Billing and Architecture

## Homework Diagrams

### Conceptual Diagram 

<img width="898" alt="image" src="https://user-images.githubusercontent.com/17580456/219206549-df03a6c9-62a2-42df-8e43-40b268aaa90f.png">

Available in [Lucidchart](https://lucid.app/lucidchart/0da8aa77-7888-45f2-a24e-936f3ebb989c/edit?viewport_loc=-641%2C60%2C2672%2C1416%2C0_0&invitationId=inv_112b39cf-ca87-4859-9c0e-b31d7c082bc8) as well. 

### Logical Diagram 

<img width="971" alt="image" src="https://user-images.githubusercontent.com/17580456/219497857-0b86f6b3-31f8-4efe-a111-67c89c2e26f1.png">

Available in [Lucidchart](https://lucid.app/lucidchart/ec42fb3c-f276-4d2b-af85-99962db59182/edit?viewport_loc=-636%2C-148%2C3072%2C1628%2C0_0&invitationId=inv_8c6fa08c-f484-4c93-8daf-9de110a47d14) as well. 

### Create Admin User 

<img width="443" alt="image" src="https://user-images.githubusercontent.com/17580456/219496165-11a9a2f0-0de9-4d66-b678-58db26e3ebe7.png">


### Install AWS CLI in gitpod 

    tasks:
      - name: aws-cli
        env:
          AWS_CLI_AUTO_PROMPT: on-partial
        init: |
          cd /workspace
          curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
          unzip awscliv2.zip
          sudo ./aws/install
          cd $THEIA_WORKSPACE_ROOT
      
Also instead of exporting the AWS credentials as [usual](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html), gitpod has as [special syntax](https://www.gitpod.io/docs/configure/projects/environment-variables) to persist them. 

### Create Budgets with AWS Cli

        aws budgets create-budget --account-id $AWS_ACCOUNT_ID --budget file://aws/json/budget.json --notifications-with-subscribers file://aws/json/notifications-with-subscribers.json
        
I see the budget on my AWS account. Remember to delete it to avoid costs. 

<img width="1540" alt="image" src="https://user-images.githubusercontent.com/17580456/219496689-d5487c11-c251-402c-99a0-53eac7f76a04.png">

### Create Billing Alarm with Cloudwatch

I followed this [tutorial](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) in AWS docs.

For that I also needed to create an SNS topic and subscribe to it which I did with the cli.

<img width="750" alt="image" src="https://user-images.githubusercontent.com/17580456/219805029-3abeb44c-5aae-4384-bd5c-f2427aa30ae4.png">

### Support Case with AWS 

At first I tried to use my personal email address to setup the bootcamp. It was an old AWS that was un-activated. I had a lot of problems due to my account not being fully activated. After trying for two days scalating the case within AWS support, I decided to re-do the setup with my LSE account. 010116213471
I wish I had done this earlier as I got really frustrated with week 0 due to this issue (I thought I was already dropping out!!) Glad I found a solution and I can continue to week1. 


