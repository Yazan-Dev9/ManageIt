from dataclasses import dataclass


@dataclass
class Employee:
    """ """

    def __init__(
        self,
        name: str = "Unknown",
        email: str = "Unknown",
        phone: str = "Unknown",
        position: str = "Unknown",
        id: int = 0
    ):
        self._id: int = id
        self._name: str = name
        self._email: str = email
        self._phone: str = phone
        # TODO make position as class than str
        self._position: str = position

    @property
    def getId(self) -> int:
        return self._id

    def setId(self, id: int):
        self._id = id

    @property
    def getName(self) -> str:
        return self._name

    def setName(self, name: str):
        self._name = name

    @property
    def getEmail(self) -> str:
        return self._email

    def setEmail(self, email: str):
        self._email = email

    @property
    def getPhone(self) -> str:
        return self._phone

    def setPhone(self, phone: str):
        self._phone = phone

    @property
    def getPosition(self) -> str:
        return self._position

    def setPosition(self, position: str):
        self._position = position
