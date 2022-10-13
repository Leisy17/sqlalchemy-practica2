
import boto3


class Get_Queue:

    def get_url_sqs(queue_name, account_id):

        sqs_client = boto3.client('sqs')

        url = sqs_client.get_queue_url(
            QueueName=queue_name,
            QueueOwnerAWSAccountId=account_id
        )
        return url
