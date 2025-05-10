from controllers.controller import IController
import datetime
from models.task import Task
from controllers.employeeController import EmployeeController


class TaskController(IController):
    """ """

    def __init__(self):
        super().__init__()
        self._task: Task = Task()
        self._rows = []

    def fetchList(self) -> list[Task]:
        """ """
        self._rows = self.getAPI.get("tasks", "*")
        tasks = []
        for row in self._rows:
            task = Task(
                row[self.TASK_TITLE],
                row[self.TASK_DESCRIPTION],
                EmployeeController().fetch(row[self.TASK_EMPLOYEE_ID]),
                datetime.date.fromisoformat(row[self.TASK_START_DATE]),
                datetime.date.fromisoformat(row[self.TASK_END_DATE]),
                row[self.TASK_STATUS],
                row[self.TASK_ID]
            )
            tasks.append(task)
        return tasks

    def fetch(self, task_id: int):
        """ """
        self._rows = self.getAPI.get("tasks", "*", "id", task_id)
        self._task.setId(self._rows[0][self.TASK_ID])
        self._task.setTitle(self._rows[0][self.TASK_TITLE])
        self._task.setDescription(self._rows[0][self.TASK_DESCRIPTION])
        self._task.setEmployee(self._rows[0][self.TASK_EMPLOYEE_ID])
        self._task.setStartDate(self._rows[0][self.TASK_START_DATE])
        self._task.setEndDate(self._rows[0][self.TASK_END_DATE])
        self._task.setStatus(self._rows[0][self.TASK_STATUS])

        return self._task

    def save(self, title, description, employee_id, start_date, end_date, status):
        """ """
        return self.getAPI.insert(
            "tasks",
            (
                "title",
                "description",
                "employee_id",
                "start_date",
                "end_date",
                "status",
            ),
            (title, description, employee_id, start_date, end_date, status),
        )

    def remove(self, task_id: int):
        return self.getAPI.delete("tasks", "task_id", task_id)

    def edit(
        self,
        task_id: int,
        title,
        description,
        employee_id,
        start_date,
        end_date,
        status,
    ):
        return self.getAPI.update(
            "tasks",
            (
                "title",
                "description",
                "employee_id",
                "start_date",
                "end_date",
                "status",
            ),
            (title, description, employee_id, start_date, end_date, status),
            "task_id",
            task_id,
        )
