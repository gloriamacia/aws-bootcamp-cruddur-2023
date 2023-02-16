# Week 0 — Billing and Architecture

## Homework Diagrams

### Conceptual Diagram 

<img width="898" alt="image" src="https://user-images.githubusercontent.com/17580456/219206549-df03a6c9-62a2-42df-8e43-40b268aaa90f.png">

Available in [Lucidchart](https://lucid.app/lucidchart/0da8aa77-7888-45f2-a24e-936f3ebb989c/edit?viewport_loc=-641%2C60%2C2672%2C1416%2C0_0&invitationId=inv_112b39cf-ca87-4859-9c0e-b31d7c082bc8) as well. 

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
