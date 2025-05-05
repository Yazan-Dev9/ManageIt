import bcrypt
from database.db import DbConnection, DbAPI


class AuthController:
    """ """

    def __init__(self):
        self.username = ""
        self.password = ""

    @staticmethod
    def checkUser(username: str, password: str):
        """ """
        hash_password = __class__()._getPasswordFromDb(username)

        return bcrypt.checkpw(password.encode("utf-8"), hash_password)

    def _getPasswordFromDb(self, username):
        """ """
        conn = DbConnection("./database/manageit.db")
        api = DbAPI(conn)
        pass_db = api.get("Users", "password", "username", username)
        stored_hashed_password = pass_db.pop()[0]
        return stored_hashed_password

    @staticmethod
    def hashedPassword(password: str):
        """ """
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password
