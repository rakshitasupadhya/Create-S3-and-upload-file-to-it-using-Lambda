# Create-S3-and-upload-file-to-it-using-Lambda
This is a simple demonstration on creating s3 bucket and uploading a json file to it using Lambda function 

# Requirement
This sample project depends on boto3, the AWS SDK for Python, and requires Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install boto3 using pip:

pip install boto3

# Project Execution
1. Create Lambda function
2. Attach Role to it - S3FullAccess
3. After executing the lambda function check if S3 bucket has been created and new file has been loaded.
4. Attach a policy in S3 to view the contents of the file

