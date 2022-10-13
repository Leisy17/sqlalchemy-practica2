from sqlalchemy import Column, Integer, String, Date
from Models.ModelBase import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    birthday = Column(Date)
    password = Column(String)
    active = Column(Integer)

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.lastname = kwargs['lastname']
        self.email = kwargs['email']
        self.birthday = kwargs['birthday']
        self.password = kwargs['password']
        self.active = kwargs['active']

    def __repr__(self):
        return """<User(name=UPPER('%s'), lastname=UPPER('%s'),
        email=LOWER('%s'), birthday='%s', password='%s')>""" % (
            self.name, self.lastname, self.email, self.birthday, self.password)
