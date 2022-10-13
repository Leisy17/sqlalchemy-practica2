

from datetime import datetime
from Classes.Images import Images
from Db.database import Methods
from Utils.Image import UploadImage
from Utils.Repeats import handler, get_body
import base64
from Utils.Upload_to_aws import upload_to_aws
import pathlib


@handler
def upload_image(event, context):
    body = get_body(event)
    base64_image = body.get('route_image')
    name = body.get('name')

    path = pathlib.Path(name)

    hashed_name = hash(name)

    base64_bytes = base64_image.encode('utf-8')
    image_bytes = base64.b64decode(base64_bytes)

    date = datetime.now()
    folder_date = datetime.strftime(date, "%Y%m%d")
    date_name = datetime.strftime(date, "%Y%m%d%H%M%S")

    file_name = f"{folder_date}/{date_name}_{hashed_name}{path.suffix}"
    message = upload_to_aws(image_bytes, file_name)

    if message:
        action = UploadImage(
            {"route_image": file_name, "name": name, "user_id": body.get('user_id')})
        msg = Images(Methods).upload_image(action)

    return msg
