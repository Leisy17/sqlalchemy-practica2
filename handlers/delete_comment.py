

from Classes.Comments import Comments
from Db.database import Methods
from Utils.Comments import DeleteComments
from Utils.Repeats import handler, get_body


@handler
def delete_comment(event, context):
    body = get_body(event)
    action = DeleteComments(body)
    msg = Comments(Methods).delete_comment(action)
    return msg
