# Week 10 — CloudFormation Part 1

### my-cluster stack on AWS Cloudformation 
<img width="1213" alt="Screenshot 2023-04-23 at 17 53 19" src="https://user-images.githubusercontent.com/17580456/233853894-2070695f-ecab-4f36-9aef-7d29a918b5cf.png">

### my-cluster stack changeset when modifying the cluster name (replacement action) 
<img width="1213" alt="Screenshot 2023-04-23 at 18 03 47" src="https://user-images.githubusercontent.com/17580456/233853903-2c2abb10-ea76-428c-a434-0e14a950c60b.png">

### my-cluster stack events list 
<img width="1529" alt="Screenshot 2023-04-23 at 18 04 52" src="https://user-images.githubusercontent.com/17580456/233853904-6e84ea28-fa59-4811-ba15-7d43ead2bd67.png">

### Creating the artifacts s3 bucket for AWS Cloudformation templates 
<img width="1386" alt="Screenshot 2023-04-23 at 18 56 12" src="https://user-images.githubusercontent.com/17580456/233853906-511f11fc-b1f5-404f-80f4-2172f11222e6.png">

### AWS Cloudformation template successfully uploaded to the s3 bucket 

```aws cloudformation deploy --stack-name "my-cluster" --s3-bucket "cfn-artifacts-cruddur-ch" --template-file $CFN_PATH --no-execute-changeset --capabilities CAPABILITY_NAMED_IAM```


<img width="1386" alt="Screenshot 2023-04-23 at 18 59 20" src="https://user-images.githubusercontent.com/17580456/233853909-021ca61a-9c9b-4d4c-9846-30077c6d0bfb.png">

### Locally downloaded AWS Cloudformation template has the correct content 
<img width="1014" alt="Screenshot 2023-04-23 at 19 02 08" src="https://user-images.githubusercontent.com/17580456/233853911-c3ab1059-ce8c-4328-a7c0-f46302bbb22b.png">
