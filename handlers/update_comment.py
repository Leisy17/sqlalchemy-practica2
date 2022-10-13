

from Classes.Comments import Comments
from Db.database import Methods
from Utils.Comments import UpdateComments
from Utils.Repeats import handler, get_body


@handler
def update_comment(event, context):
    body = get_body(event)
    action = UpdateComments(body)
    msg = Comments(Methods).update_comment(action)
    return msg
