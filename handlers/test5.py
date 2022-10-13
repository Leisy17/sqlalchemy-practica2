
from os import environ
from Utils.Repeats import handler, get_body
from Utils.Sns import SNSInvoke


@handler
def test5(event, context):
    body = get_body(event)
    data = SNSInvoke.create_sns_subscription(
        body, environ.get('SNS_TOPIC_ARN'))
    if data['ResponseMetadata']["HTTPStatusCode"] == 200:
        msg = {"msg": "Comentario creado satisfactoriamente"}
    else:
        msg = {"msg": "Error: Fallo en creación de comentario"}
    return msg
