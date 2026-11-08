import unittest
from User import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("Mariam", "mariam", "1234")

    def test_login_success(self):
        self.assertTrue(self.user.login("mariam", "1234"))

    def test_login_wrong_password(self):
        self.assertFalse(self.user.login("mariam", "wrong"))

    def test_login_wrong_username(self):
        self.assertFalse(self.user.login("wrong", "1234"))


if __name__ == "__main__":
    unittest.main()
