import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()
print("test")
# Print bucket names
print("S3 Buckets:")
for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    print(f"- {bucket['Name']}")

bucket_name = 'your_bucket_name'
object_key = 'uploaded.txt'
file_path = 'path/to/your/local/file.txt'  # Replace with the path to the file you want to upload

# Create an S3 client
s3 = boto3.client('s3')

# Upload the file to the S3 bucket
s3.upload_file(file_path, bucket_name, object_key)

print(f"File uploaded successfully to {bucket_name}/{object_key}")