from service import UserService
from entity import User

class MysqlRPC(object):
    __user_service = None

    def __init__(self):
        self.__user_service = UserService()

    def save_user(self, username, password, email):
        user = User(username=username, password=password, email=email)
        self.__user_service.save(user)

    def update_user(self, username, password, email):
        user = User(username=username, password=password, email=email)
        self.__user_service.update(user)

    def find_user_by_id(self, id):
        self.__user_service.find(id)

    def delete_user(self, id):
        self.__user_service.delete(id)
