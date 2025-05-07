from dataclasses import dataclass


@dataclass
class Role:
    def __init__(self, id: int = 0, name: str = "Unknown"):
        self._id = id
        self.role_name = name

    @property
    def getId(self) -> int:
        return self._id

    def setId(self, id: int):
        self._id = id

    @property
    def getName(self) -> str:
        return self._role_name

    def setName(self, name: str):
        self._role_name = name
