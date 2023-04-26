## Architecture Guide

Before you run any templates, be sure to create an S3 bucket to contain
all of our artifacts for CloudFormation.

```
aws s3 mk s3://cfn-artifacts-cruddur-ch
export CFN_BUCKET="cfn-artifacts-cruddur-ch"
gp env CFN_BUCKET="cfn-artifacts-cruddur-ch"
```