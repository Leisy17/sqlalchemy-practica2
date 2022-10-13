
from Classes.News import News
from Db.database import Methods
from Utils.News import DeleteNews
from Utils.Repeats import handler, get_body


@handler
def delete_new(event, context):
    body = get_body(event)
    action = DeleteNews(body)
    msg = News(Methods).delete_new(action)
    return msg
