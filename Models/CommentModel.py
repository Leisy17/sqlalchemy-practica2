from sqlalchemy import Column, Integer, String
from Models.ModelBase import Base


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    comment = Column(String)
    user_id = Column(Integer)
    new_id = Column(Integer)
    active = Column(Integer)

    def __init__(self, **kwargs):
        self.comment = kwargs['comment']
        self.user_id = kwargs['user_id']
        self.new_id = kwargs['new_id']

    def __repr__(self):
        return """<Comment(comment='%s', user_id='%s',
        new_id='%s')>""" % (
            self.comment, self.user_id, self.new_id)
