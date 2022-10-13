
from Classes.Users import Users
from Db.database import Methods
from Utils.Users import DeleteUsers
from Utils.Repeats import handler, get_body


@handler
def delete_user(event, context):
    body = get_body(event)
    action = DeleteUsers(body)
    msg = Users(Methods).delete_user(action)
    return msg
