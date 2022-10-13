from sqlalchemy import Column, Integer, String
from Models.ModelBase import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    profession = Column(String)

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.profession = kwargs['profession']

    def __repr__(self):
        return """<User(user_id='%s', profession=UPPER('%s')>""" % (
            self.user_id, self.profession)
