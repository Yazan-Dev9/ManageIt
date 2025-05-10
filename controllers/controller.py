from abc import ABC, abstractmethod
from database.dbapi import DbAPI
from database.dbconnection import DbConnection


class IController(ABC):

    USER_ID = EMPLOYEE_ID = TASK_ID = 0
    USER_USERNAME = EMPLOYEE_NAME = TASK_TITLE = 1
    USER_PASSWORD = EMPLOYEE_EMAIL = TASK_DESCRIPTION = 2
    USER_FULL_NAME = EMPLOYEE_PHONE = TASK_EMPLOYEE_ID = 3
    USER_ROLE_ID = EMPLOYEE_POSITION = TASK_START_DATE = 4
    USER_EMPLOYEE_ID = TASK_END_DATE = 5
    TASK_STATUS = 6

    def __init__(self):
        conn = DbConnection("./database/manageit.db")
        self._api = DbAPI(conn)

    @abstractmethod
    def fetchList(self, *arges, **kwargs) -> list:
        pass

    @abstractmethod
    def fetch(self, *arges, **kwargs) -> object:
        pass

    @abstractmethod
    def save(self, *arges, **kwargs) -> bool:
        pass

    @abstractmethod
    def remove(self, *arges, **kwargs) -> bool:
        pass

    @abstractmethod
    def edit(self, *arges, **kwargs) -> bool:
        pass

    @property
    def getAPI(self) -> DbAPI:
        return self._api
