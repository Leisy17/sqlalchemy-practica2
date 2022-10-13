import json
import boto3


class Invoke:

    def invoke(data, lambdaf):
        lambda_client = boto3.client('lambda')
        lambda_payload = json.dumps({
            "body": data,
            "httpMethod": "POST"
        })
        return lambda_client.invoke(FunctionName=lambdaf,
                                    InvocationType='RequestResponse',
                                    Payload=lambda_payload)
