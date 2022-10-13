from Db.database import Methods
from Models.NewModel import New
from Utils.News import CreateNews, DeleteNews, UpdateNews
from sqlalchemy import insert, select, update


class News:
    def __init__(self, db: Methods) -> None:
        self.db = db

    def create_new(self, data: CreateNews):
        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        stmt = insert(New).values(data)
        result = self.db.create(stmt)
        return {"msg": "Se ha creado la noticia satisfactoriamente",
                "id": result}

    def update_new(self, data: UpdateNews):
        stmt = select(New).where(New.id == data['id'])
        result = self.db.get(stmt)
        if not result:
            raise ValueError("Credenciales inválidas o noticia no existe")

        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        if (type(data["id"]) is not int or type(data["abstract"]) is not str or
                type(data["abstract"]) is not str or type(data["description"])
                is not str):
            raise ValueError("Datos inválidos")

        stmt = update(New).where(New.id == data['id']).values(
            title=data['title'],
            abstract=data['abstract'],
            description=data['description'])
        self.db.update(stmt)

        return {"msg": "Actualización de noticia satisfactoria"}

    def delete_new(self, data: DeleteNews):

        stmt = select(New).where(New.id == data['id'])
        result = self.db.get(stmt)

        if not result:
            raise ValueError("Este comentario no existe")

        stmt = update(New).where(New.id == data['id']).values(
            active=0)
        self.db.update(stmt)

        return {"msg": "Este comentario ha sido eliminado"}
