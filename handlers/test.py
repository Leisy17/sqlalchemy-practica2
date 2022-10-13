

from Utils.Invoke import Invoke
from Utils.Repeats import handler, get_body
import os
import json


@handler
def test(event, context):
    body = get_body(event)
    print("body:", body)
    data = Invoke.invoke(body, os.environ.get('LambdaComment'))
    read = data['Payload'].read()
    print("invoke:", read)
    load_data = json.loads(read)
    return load_data
