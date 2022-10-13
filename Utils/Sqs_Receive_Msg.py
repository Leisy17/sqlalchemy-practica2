
import boto3


class Receive_SQS:

    def receive_sqs(queue_url):
        sqs = boto3.client('sqs')
        # Send message to SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url
        )
        if not response:
            raise Exception(
                f'No es posible recibir el mensaje desde {queue_url}')
        else:
            return response
