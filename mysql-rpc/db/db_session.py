from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .settings import *

class DBSession(object):
    __db_url = "%s://%s:%s@%s:%s/%s" % (
            DATABASE_TYPE,
            DATABASE_USERNAME,
            DATABASE_PASSWORD,
            DATABASE_HOST,
            DATABASE_PORT,
            DATABASE_SCHEMA
        )
    __instance = None
    __engine = None
    __maker = object
    __session = None

    def __init__(self):
        if not DBSession.__instance:
            # initialization
            self.__engine = create_engine(self.__db_url, echo=True)
            self.__maker = sessionmaker(bind=self.__engine)
        else:
            # __call__
            pass

    @staticmethod
    def getInstance():
        if not DBSession.__instance:
            DBSession.__instance = DBSession()
        return DBSession.__instance

    @classmethod
    def getSession(self):
        if not self.__engine:
            self.__engine = create_engine(self.__db_url, echo=True)
            self.__maker = sessionmaker(bind=self.__engine)
            self.__session = self.__maker()
        return self.__session

    @classmethod
    def getEngine(self):
        if not self.__engine:
            self.__engine = create_engine(self.__db_url, echo=True)
        return self.__engine

    @classmethod
    def close(self):
        self.__session.commit()
        self.__session.close()
        self.__session = None
