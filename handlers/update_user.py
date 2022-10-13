

from Classes.Users import Users
from Db.database import Methods
from Utils.Users import CreateUsers
from Utils.Repeats import handler, get_body


@handler
def update_user(event, context):
    body = get_body(event)
    action = CreateUsers(body)
    msg = Users(Methods).update_user(action)
    if not action:
        Exception("""El formato para la fecha de cumpleaños debe ser
        YYYY-MM-DD""")
    return msg
