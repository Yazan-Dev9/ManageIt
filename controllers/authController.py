import bcrypt
from database.dbconnection import DbConnection
from database.dbapi import DbAPI
from models.user import User


class AuthController:
    """ """

    ID = 0
    USERNAME = 1
    PASSWORD = 2
    FULL_NAME = 3
    ROLE_ID = 4
    EMPLOYEE_ID = 5

    def __init__(self):
        self._user: User = User()
        self._rows = []

    def checkUser(self, username: str, password: str):
        """ """
        hash_password = self._getHashPassword(username)

        return bcrypt.checkpw(password.encode("utf-8"), hash_password)  # type: ignore

    def _getHashPassword(self, username):
        """ """
        self.fetchUser(username)
        stored_hashed_password = self._user.getPassword

        return stored_hashed_password

    def fetchUser(self, username: str):
        """ """
        conn = DbConnection("./database/manageit.db")
        self.api = DbAPI(conn)
        self._rows = self.api.get("Users", "*", "username", username)
        self._user.setId(self._rows[0][self.ID])
        self._user.setUserName(self._rows[0][self.USERNAME])
        self._user.setPassword(self._rows[0][self.PASSWORD])
        self._user.setFullName(self._rows[0][self.FULL_NAME])
        self._user.setRole(self._rows[0][self.ROLE_ID])

        return self._user

    @property
    def getUser(self):
        return self._user

    @staticmethod
    def hashedPassword(password: str):
        """ """
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password
