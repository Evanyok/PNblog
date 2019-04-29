from db import DBSession
from entity import User

class UserService(object):

    __db = None

    def __init__(self):
        self.__db = DBSession.getInstance()
        User.create(self.__db.getEngine())

    # create
    def save(self, user):
        if user is User:
            user = self.__db.getSession().add(user)
            self.__db.close()
        return user.username

    # update
    def update(self, user):
        if user is User:
            self.__db.getSession().query(User).filter(User.id == id).one().update().values(
                username = user.username, password = user.password, email = user.email)
            self.__db.getSession().close()
            return True

    # read
    def find(self, id):
        user = self.__db.getSession().query(User).filter(User.id == id).one()
        self.__db.getSession().close()
        return user
    
    # delete
    def delete(self, id):
        self.__db.getSession().query(User).filter(User.id == id).one().delete()
        self.__db.getSession().close()
        return True