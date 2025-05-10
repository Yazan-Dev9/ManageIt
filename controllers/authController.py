import bcrypt
from models.user import User
from controllers.controller import IController


class AuthController(IController):
    """ """

    def __init__(self):
        super().__init__()
        self._user: User = User()
        self._rows = []

    def checkUser(self, username: str, password: str):
        """ """
        hash_password = self._getHashPassword(username)

        return bcrypt.checkpw(password.encode("utf-8"), hash_password)  # type: ignore

    def _getHashPassword(self, username):
        """ """
        self.fetch(username)
        stored_hashed_password = self.getUser.getPassword

        return stored_hashed_password

    def fetch(self, username: str):
        """ """
        self._rows = self.getAPI.get("Users", "*", "username", username)
        self._user.setId(self._rows[0][self.USER_ID])
        self._user.setUserName(self._rows[0][self.USER_USERNAME])
        self._user.setPassword(self._rows[0][self.USER_PASSWORD])
        self._user.setFullName(self._rows[0][self.USER_FULL_NAME])
        self._user.setRole(self._rows[0][self.USER_ROLE_ID])

        return self._user

    def save(self, username: str, password: str, fullname: str, role: int):
        """ """
        hashed_password = self.hashedPassword(password)
        return self.getAPI.insert(
            "Users",
            (
                "username",
                "password",
                "full_name",
                "role_id",
            ),
            (
                username,
                hashed_password,
                fullname,
                role,
            ),
        )

    def fetchList(self, *arges, **kwargs) -> list:
        return super().fetchList(*arges, **kwargs)

    def remove(self, *arges, **kwargs):
        return super().remove(*arges, **kwargs)

    def edit(self, *arges, **kwargs):
        return super().remove(*arges, **kwargs)

    @property
    def getUser(self):
        return self._user

    @staticmethod
    def hashedPassword(password: str):
        """ """
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password
