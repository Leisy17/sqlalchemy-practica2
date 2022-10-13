
import boto3
from botocore.exceptions import NoCredentialsError
import os


def generate_presigned_url(route_file):
    s3 = boto3.client('s3')

    try:
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': os.environ['BUCKET_NAME'],
                'Key': route_file
            },
            ExpiresIn=24 * 3600
        )

        print("Upload Successful", url)
        return url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None
