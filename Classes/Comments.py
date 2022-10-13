from Db.database import Methods
from Models.CommentModel import Comment
from Models.NewModel import New
from Models.UserModel import User
from Utils.Comments import CreateComments, DeleteComments, GetComments
from Utils.Comments import UpdateComments
from sqlalchemy import insert, select, update


class Comments:

    def __init__(self, db: Methods) -> None:
        self.db = db

    def create_comment(self, data: CreateComments):
        stmt_user = select(User).where(User.id == data['user_id'])
        result_user = self.db.get(stmt_user)

        stmt_new = select(New).where(New.id == data['new_id'])
        result_new = self.db.get(stmt_new)

        if not result_user:
            raise ValueError("Este usuario no existe")

        if not result_new:
            raise ValueError("Esta noticia no existe")

        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        if (type(data["comment"]) is not str or type(data["user_id"]) is not
                int or type(data["new_id"]) is not int):
            raise ValueError("Datos inválidos")

        stmt = insert(Comment).values(data)
        result = self.db.create(stmt)

        return {"msg": "Comentario creado satisfactoriamente", "id": result}

    def update_comment(self, data: UpdateComments):
        stmt = select(Comment).where(Comment.id == data['id'])
        result = self.db.get(stmt)

        if not result:
            raise ValueError("Este comentario no existe")

        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        if type(data["comment"]) is not str or type(data["id"]) is not int:
            raise ValueError("Datos inválidos")

        stmt = update(Comment).where(Comment.id == data['id']).values(
            comment=data['comment'])
        self.db.update(stmt)

        return {"msg": "Comentario actualizado correctamente"}

    def delete_comment(self, data: DeleteComments):

        stmt = select(Comment).where(Comment.id == data['id'])
        result = self.db.get(stmt)

        if not result:
            raise ValueError("Este comentario no existe")

        if type(data["id"]) is not int:
            raise ValueError("Datos inválidos")

        stmt = update(Comment).where(Comment.id == data['id']).values(
            active=0)
        self.db.update(stmt)

        return {"msg": "Este comentario ha sido eliminado"}

    def get_comment(self, data: GetComments):

        stmt_new = select(New.id).where(New.id == data['new_id'])
        result = self.db.get(stmt_new)

        if not result:
            raise ValueError("Esta noticia no existe")

        stmt = select(
            Comment.comment, User.name, User.lastname
        ).join(
            User, Comment.user_id == User.id
        ).where(
            Comment.new_id == data['new_id'],
            Comment.active == 1,
            User.active == 1
        )

        msg = self.db.get(stmt)

        return msg
