from controllers.controller import IController
from models.employee import Employee


class EmployeeController(IController):
    """ """

    def __init__(self):
        super().__init__()
        self._employee: Employee = Employee()
        self._rows = []

    def fetchList(self) -> list[Employee]:
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

    def fetch(self, employee_id: int):
        """ """
        self._rows = self.getAPI.get("Employees", "*", "employee_id", employee_id)
        self._employee.setId(self._rows[0][self.EMPLOYEE_ID])
        self._employee.setName(self._rows[0][self.EMPLOYEE_NAME])
        self._employee.setEmail(self._rows[0][self.EMPLOYEE_EMAIL])
        self._employee.setPhone(self._rows[0][self.EMPLOYEE_PHONE])
        self._employee.setPosition(self._rows[0][self.EMPLOYEE_POSITION])

        return self._employee

    def save(self, name, email, phone, position):
        """ """
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

    def remove(self, employee_id: int):
        return self.getAPI.delete("Employees", "employee_id", employee_id)

    def edit(self, employee_id: int, name, email, phone, position):
        return self.getAPI.update(
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
            "employee_id",
            employee_id,
        )
