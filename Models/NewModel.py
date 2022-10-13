from sqlalchemy import Column, Integer, String
from Models.ModelBase import Base


class New(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    abstract = Column(String)
    description = Column(String)
    author_id = Column(Integer)
    active = Column(Integer)

    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.abstract = kwargs['abstract']
        self.description = kwargs['description']
        self.author_id = kwargs['author_id']
        self.active = kwargs['active']

    def __repr__(self):
        return """<New(title=UPPER('%s'), abstract=UPPER('%s'),
        description=UPPER('%s'), author_id='%s', active='%s)>""" % (
            self.title, self.abstract, self.description, self.author_id,
            self.active)
