from Db.database import Methods
from Models.AuthorModel import Author
from Utils.Authors import CreateAuthors
from sqlalchemy import insert, select


class Authors:

    def __init__(self, db: Methods) -> None:
        self.db = db

    def create_author(self, data: CreateAuthors):

        stmt = select(Author).where(Author.user_id == data['user_id'])
        result = self.db.get(stmt)

        if result:
            raise ValueError("El autor ya existe")

        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        if not data["profession"] and not data["user_id"]:
            raise Exception("Todos los campos son necesarios")

        if (type(data["profession"]) is not str
                or type(data["user_id"]) is not int):
            raise ValueError("Datos inválidos")

        stmt = insert(Author).values(data)
        result = self.db.create(stmt)

        return {"msg": "Se ha agregado el autor correctamente", "id": result}
