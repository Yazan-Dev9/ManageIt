from dataclasses import dataclass
from datetime import date
from typing import Optional

from models.employee import Employee


@dataclass
class Task:
    """ """

    def __init__(
        self,
        id: int = 0,
        title: str = "Unknown",
        description: str = "Unknown",
        employee: Optional[Employee] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        status: str = "Unknown"
    ):
        self._id: int = id
        self._title: str = title
        self._description: str = description
        self._employee: Optional[Employee] = employee
        self._start_date: Optional[date] = start_date
        self._end_date: Optional[date] = end_date
        # TODO Make status as class than str
        self._status: str = status

    @property
    def getId(self) -> int:
        return self._id

    def setId(self, id: int):
        self._id = id

    @property
    def getTitle(self) -> str:
        return self._title

    def setTitle(self, title: str):
        self._title = title

    @property
    def getDescription(self) -> str:
        return self._description

    def setDescription(self, description: str):
        self._description = description

    @property
    def getEmployee(self) -> Optional[Employee]:
        return self._employee

    def setEmployee(self, employee: Employee):
        self._employee = employee

    @property
    def getStartDate(self) -> Optional[date]:
        return self._start_date

    def setStartDate(self, start_date: date):
        self._start_date = start_date

    @property
    def getEndDate(self) -> Optional[date]:
        return self._end_date

    def setEndDate(self, end_date: date):
        self._end_date = end_date

    @property
    def getStatus(self) -> str:
        return self._status

    def setStatus(self, status: str):
        self._status = status
