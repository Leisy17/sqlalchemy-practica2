

from Classes.Images import Images
from Db.database import Methods
from Utils.Image import DownloadImage
from Utils.Repeats import get_body, handler
from Utils.Download_from_aws import generate_presigned_url


@handler
def get_image(event, context):
    body = get_body(event)
    action = DownloadImage(body)
    msg = Images(Methods).download_image(action)
    if msg:
        val = msg[0]
        route = val.get('route_image', '')
        msg = generate_presigned_url(route)
    return msg
