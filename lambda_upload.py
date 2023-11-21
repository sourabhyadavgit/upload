import json
import boto3
from botocore.exceptions import ClientError
import logging
import base64


log_group_name = 'your-log-group-name'
log_stream_name = 'your-log-stream-name'
region_name = 'your-region'

# Create a CloudWatch Logs client
logs_client = boto3.client('logs', region_name='us-east-1')

s3 = boto3.client('s3')



def lambda_handler(event, context):
    #print("------")
    #print(event)
    #print("------")
    #logging.info("Received event: %s", event)
    try:
        # Extract information from the API Gateway event
        bucket_name = 'sourabh13062023'
        object_key = 'uploaded.docx'  
        file_content = base64.b64decode(event['content'])
        #base64.b64decode(event['body'])
        #filecontent_decypted = base64.b64decode(file_content)
        
        # Upload the file content to S3
        s3.put_object(Body=file_content, Bucket=bucket_name, Key=object_key)

        return {
            'statusCode': 200,
            'body': json.dumps(f"File {object_key} uploaded successfully to {bucket_name}")
        }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error uploading file: {e}")
        }
