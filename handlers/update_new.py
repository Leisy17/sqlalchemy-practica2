

from Classes.News import News
from Db.database import Methods
from Utils.News import UpdateNews
from Utils.Repeats import handler, get_body


@handler
def update_new(event, context):
    body = get_body(event)
    action = UpdateNews(body)
    msg = News(Methods).update_new(action)
    return msg
