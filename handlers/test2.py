

from Utils.Invoke_async import Invoke_A
from Utils.Repeats import handler, get_body
import os


@handler
def test2(event, context):
    body = get_body(event)
    print("body:", body)
    data = Invoke_A.invoke_async(body, os.environ.get('LambdaComment'))
    if data['StatusCode'] == 202:
        msg = {"msg": "Comentario creado satisfactoriamente"}
    else:
        msg = {"msg": "Error: Fallo en creación de comentario"}
    return msg
