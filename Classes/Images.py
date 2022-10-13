
from Db.database import Methods
from Models.ImagesModel import Image
from Models.UserModel import User
from Utils.Image import DownloadImage, UploadImage
from sqlalchemy import insert, select


class Images:

    def __init__(self, db: Methods) -> None:
        self.db = db

    def upload_image(self, data: UploadImage):
        stmt = select(User).where(User.id == data['user_id'])
        result = self.db.get(stmt)

        if not result:
            raise ValueError("El usuario no existe")

        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        stmt = insert(Image).values(data)
        result = self.db.create(stmt)

        return {"msg": "Se ha agregado la imagen correctamente", "id": result}

    def download_image(self, data: DownloadImage):

        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        stmt = select(
            Image.route_image, User.name, User.lastname, Image.name
        ).join(
            User, Image.user_id == User.id
        ).where(
            Image.id == data['id'],
            Image.user_id == data['user_id'],
            Image.active == 1,
            User.active == 1
        )

        msg = self.db.get(stmt)

        return msg
