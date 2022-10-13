

from Utils.Get_Queue_Url import Get_Queue
from Utils.Repeats import handler, get_body
from os import environ

from Utils.Sqs_Invoke import Invoke_SQS


@handler
def test3(event, context):
    body = get_body(event)
    get_url_queue = Get_Queue.get_url_sqs(environ.get('QUEUE_NAME'),
                                          environ.get('QUEUEOWNERAWSACCOUNTID'
                                                      ))

    data = Invoke_SQS.invoke_sqs(get_url_queue['QueueUrl'], body)
    if data['ResponseMetadata']["HTTPStatusCode"] == 200:
        msg = {"msg": "Comentario creado satisfactoriamente"}
    else:
        msg = {"msg": "Error: Fallo en creación de comentario"}
    return msg
