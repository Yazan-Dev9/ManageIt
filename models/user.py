from dataclasses import dataclass
from typing import Optional

from models.employee import Employee
from models.role import Role


@dataclass
class User:
    """ """

    def __init__(
        self,
        id: int = 0,
        username: str = "Unknown",
        password: str = "Unknown",
        full_name: str = "Unknown",
        role: Optional[Role] = None,
        employee: Optional[Employee] = None
    ):
        self._id: int = id
        self._username: str = username
        self._password: str = password
        self._full_name: str = full_name
        self._role: Optional[Role] = role
        self._employee: Optional[Employee] = employee

    @property
    def getId(self) -> int:
        return self._id

    def setId(self, id: int):
        self._id = id

    @property
    def getUserName(self) -> str:
        return self._username

    def setUserName(self, username: str):
        self._username = username

    @property
    def getPassword(self) -> str:
        return self._password

    def setPassword(self, password: str):
        self._password = password

    @property
    def getFullName(self) -> str:
        return self._full_name

    def setFullName(self, full_name: str):
        self._full_name = full_name

    @property
    def getRole(self) -> Optional[Role]:
        return self._role

    def setRole(self, role: Role):
        self._role = role

    @property
    def getEmployee(self) -> Optional[Employee]:
        return self._employee

    def setEmployee(self, employee: Employee):
        self._employee = employee
