from database.dbconnection import DbConnection
from database.dbapi import DbAPI
from models.employee import Employee


class Controller:

    USER_ID = 0
    USER_USERNAME = 1
    USER_PASSWORD = 2
    USER_FULL_NAME = 3
    USER_ROLE_ID = 4
    USER_EMPLOYEE_ID = 5
    EMPLOYEE_ID = 0
    EMPLOYEE_NAME = 1
    EMPLOYEE_EMAIL = 2
    EMPLOYEE_PHONE = 3
    EMPLOYEE_POSITION = 4

    def __init__(self):
        conn = DbConnection("./database/manageit.db")
        self.api = DbAPI(conn)

    @property
    def getAPI(self):
        return self.api


class EmployeeController(Controller):
    """ """

    def __init__(self):
        super().__init__()
        self._employee: Employee = Employee()
        self._rows = []

    def fetchEmployees(self) -> list[Employee]:
        """ """
        self._rows = self.getAPI.get("Employees", "*")
        employees = []
        for row in self._rows:
            employee = Employee(
                row[self.EMPLOYEE_NAME],
                row[self.EMPLOYEE_EMAIL],
                row[self.EMPLOYEE_PHONE],
                row[self.EMPLOYEE_POSITION],
                row[self.EMPLOYEE_ID],
            )
            employees.append(employee)
        return employees

    def saveEmployee(self, name, email, phone, position):
        return self.getAPI.insert(
            "Employees",
            (
                "name",
                "email",
                "phone",
                "position",
            ),
            (
                name,
                email,
                phone,
                position,
            ),
        )
