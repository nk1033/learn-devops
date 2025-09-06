## Create aws S3 Bucket using boto3 module.

import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket = 'My-new-Bucket-boto3',
)

### Get Bucket ACL

import boto3

client = boto3.client('s3')

response = client.get_bucket_acl(
    Bucket = 'My-new-Bucket-boto3',
)
print(response)


## boto3 will support both client & resource to interact with the services. But for future boto3 will no longer support resources.
## boto3 have botocore inbuilt functionalities which will handle exceptions like try-catch , error-handling

