
from Db.database import Methods
from Models.UserModel import User
from Utils.Repeats import validate_date
from Utils.Users import CreateUsers, DeleteUsers
from sqlalchemy import insert, select, update


class Users:

    def __init__(self, db: Methods) -> None:
        self.db = db

    def register_user(self, data: CreateUsers):
        stmt = select(User).where(User.email == data['email'])
        result = self.db.get(stmt)

        if result:
            raise ValueError("El usuario ya existe")

        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        validate_date(data["birthday"])

        stmt = insert(User).values(data)
        result = self.db.create(stmt)

        return {"msg": "Se ha agregado el usuario correctamente", "id": result}

    def update_user(self, data: CreateUsers):

        stmt = select(User).where(
            User.email == data['email'], User.password == data['password'])
        result = self.db.get(stmt)

        if not result:
            raise ValueError("Credenciales inválidas")

        for value in data.values():
            if not value:
                raise ValueError("Todos los campos son necesarios")

        stmt = update(User).where(User.email == data['email'],
                                  User.password ==
                                  data['password']).values(
            name=data['name'], lastname=data['lastname'],
            birthday=data['birthday'])

        self.db.update(stmt)

        return {"msg": "Actualización de usuario satisfactoria"}

    def delete_user(self, data: DeleteUsers):

        stmt = select(User).where(
            User.email == data['email'], User.password == data['password'])
        result = self.db.get(stmt)

        if not result:
            raise ValueError("Este usuario no existe")

        if (type(data["email"]) is not str and type(data["password"]) is not
                str):
            raise ValueError("Datos inválidos")

        stmt = update(User).where(User.email == data['email'],
                                  User.password == data["password"]).values(
            active=0)
        self.db.update(stmt)

        return {"msg": "Este usuario ha sido eliminado"}
