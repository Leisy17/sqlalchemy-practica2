

from Classes.News import News
from Db.database import Methods
from Utils.News import CreateNews
from Utils.Repeats import handler, get_body


@handler
def create_new(event, context):
    body = get_body(event)
    action = CreateNews(body)
    msg = News(Methods).create_new(action)
    return msg
