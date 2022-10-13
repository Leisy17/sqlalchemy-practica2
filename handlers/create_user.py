

from Classes.Users import Users
from Db.database import Methods
from Utils.Users import CreateUsers
from Utils.Repeats import handler, get_body


@handler
def create_user(event, context):
    body = get_body(event)
    action = CreateUsers(body)
    msg = Users(Methods).register_user(action)
    return msg
