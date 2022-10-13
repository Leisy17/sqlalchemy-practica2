

from Classes.Comments import Comments
from Db.database import Methods
from Utils.Comments import GetComments
from Utils.Repeats import get_body, handler


@handler
def get_comment(event, context):
    body = get_body(event)
    action = GetComments(body)
    msg = Comments(Methods).get_comment(action)
    return msg
