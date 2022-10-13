

from Classes.Authors import Authors
from Db.database import Methods
from Utils.Authors import CreateAuthors
from Utils.Repeats import handler, get_body


@handler
def create_author(event, context):
    body = get_body(event)
    action = CreateAuthors(body)
    msg = Authors(Methods).create_author(action)
    return msg
