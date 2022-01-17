# Service that (Creates thumbnail when uploaded an Png file in the S3 Bucket) using Serverless

## Prerequisite :
1. Node and Npm
2. Setup Serverless
3. Aws cli
4. Python and Boto3
5. Serverless-python-requirements

## Steps :-

1. Create project folder 
```
sls create --template aws-python3 --path s3-thumbnail-generator
```
2. Create lambda function i.e handler.py
3. Create Roles, Specify Event i.e yaml file
4. Deploy the code
```
sls deploy --verbose
```
5. Try uploading a png file in S3 bucket
6. Refresh and see if any thumbnail file is created or not
