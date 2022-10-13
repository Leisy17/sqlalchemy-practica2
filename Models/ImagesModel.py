from sqlalchemy import Column, Integer, String
from Models.ModelBase import Base


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    route_image = Column(String)
    user_id = Column(Integer)
    active = Column(Integer)

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.route_image = kwargs['route_image']
        self.user_id = kwargs['user_id']
        self.active = kwargs['active']

    def __repr__(self):
        return """<Image(name='%s', route_image='%s',
        user_id='%s', active='%s')>""" % (
            self.name, self.route_image, self.user_id, self.active)
