
from Classes.Comments import Comments
from Db.database import Methods
from Utils.Comments import CreateComments
from Utils.Repeats import get_body, handler


@handler
def create_comment(event, context):
    body = get_body(event)
    action = CreateComments(body)
    msg = Comments(Methods).create_comment(action)
    return msg
