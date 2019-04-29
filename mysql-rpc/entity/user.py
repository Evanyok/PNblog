from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class User(Base):

    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(128))
    email = Column(String(64))

    @staticmethod
    def create(engine):
        User.metadata.create_all(engine, checkfirst=True)

    def __repr__(self):
        return "<User(id='%d', username='%s', email='%s')>" % (self.id, self.username, self.email)