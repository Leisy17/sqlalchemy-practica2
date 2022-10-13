
from Utils.Random_String import RandomString
import boto3
import json


class Invoke_SQS:

    def invoke_sqs(queue_url, data):
        sqs = boto3.client('sqs')

        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageGroupId=RandomString.get_random_string(),
            MessageBody=json.dumps(data)
        )
        if not response:
            raise Exception(
                f'No es posible recibir el mensaje desde {queue_url}')
        else:
            return response
