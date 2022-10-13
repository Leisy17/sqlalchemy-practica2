
import boto3
from botocore.exceptions import NoCredentialsError
import os


def upload_to_aws(object_file, route_file):
    s3 = boto3.client('s3')

    try:
        s3.put_object(
            Body=object_file,
            Bucket=os.environ['BUCKET_NAME'],
            Key=route_file,)
        return {"msg": "Upload Succesfully"}

    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None
