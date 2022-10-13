import json
import boto3


class SNSInvoke:
    def create_sns_subscription(message, target_arn):
        client = boto3.client('sns')
        response = client.publish(
            TargetArn=target_arn,
            Message=json.dumps(message)
        )
        return response
