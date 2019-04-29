from db import DBSession
from entity import User
from service import UserService
import unittest

class TestUserService(unittest.TestCase):
    def test_save(self):
        u = User(
            username = 't1',
            password = '1234',
            email = 't1@test.com'
        )

        us = UserService()
        us.find(5)

if __name__ == "__main__":
    unittest.main()
