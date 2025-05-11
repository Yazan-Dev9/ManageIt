import bcrypt
from models.role import Role
from models.user import User
from controllers.controller import IController


class AuthController(IController):
    """ """

    def __init__(self):
        super().__init__()
        self._user: User = User()
        self._role: Role = Role()
        self._rows = []

    def checkUser(self, username: str, password: str) -> bool:
        """
        Check if username exists and password matches.
        """
        user = self.fetch(username)
        if not user:
            return False

        stored_hashed_password = user.getPassword

        if isinstance(stored_hashed_password, str):
            stored_hashed_password = stored_hashed_password.encode("utf-8")

        return bcrypt.checkpw(password.encode("utf-8"), stored_hashed_password)

    def fetch(self, username: str):
        """ """
        self._rows = self.getAPI.get("Users", "*", "username", username)

        if not self._rows:
            return None

        self._user.setId(self._rows[0][self.USER_ID])
        self._user.setUserName(self._rows[0][self.USER_USERNAME])
        self._user.setPassword(self._rows[0][self.USER_PASSWORD])
        self._user.setFullName(self._rows[0][self.USER_FULL_NAME])
        self._user.setRole(self._getRoleById(self._rows[0][self.USER_ROLE_ID]))  # type: ignore

        return self._user

    def fetchRole(self, name: str):
        """ """
        self._rows = self.getAPI.get("Role", "*", "role_name", name)
        if not self._rows:
            return None

        self._role.setId(self._rows[0][self.ROLE_ID])
        self._role.setName(self._rows[0][self.ROLE_NAME])

        return self._role

    def _getRoleById(self, id: int):
        self._rows = self.getAPI.get("Role", "*", "role_id", id)
        if not self._rows:
            return None

        self._role.setId(id)
        self._role.setName(self._rows[0][self.ROLE_NAME])

        return self._role

    def save(self, username: str, password: str, full_name: str, role_id: int):
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
                full_name,
                role_id,
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

    @property
    def getRole(self):
        return self._role

    @staticmethod
    def hashedPassword(password: str):
        """ """
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password
