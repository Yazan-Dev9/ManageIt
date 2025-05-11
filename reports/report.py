from database.dbconnection import DbConnection


class Report:
    def __init__(self):
        self._conn = DbConnection("./database/manageit.db")

    def getCompleted(self):
        result = self._conn.executeQuery(
            """SELECT
                    name,
                    COUNT(Tasks.task_id) AS total_tasks,
                    SUM(CASE WHEN Tasks.status = ? THEN 1 ELSE 0 END) AS completed_tasks
                    FROM Employees
                    INNER JOIN Tasks ON Employees.employee_id = Tasks.employee_id
                    GROUP BY Employees.employee_id, Employees.name""",
            ("Completed",),
        )
        return result

    def getProgress(self):
        result = self._conn.executeQuery(
            """SELECT
                    name,
                    COUNT(Tasks.task_id) AS total_tasks,
                    SUM(CASE WHEN Tasks.status = ? THEN 1 ELSE 0 END) AS completed_tasks
                    FROM Employees
                    INNER JOIN Tasks ON Employees.employee_id = Tasks.employee_id
                    GROUP BY Employees.employee_id, Employees.name""",
            ("Progress",),
        )
        return result


# reports/report.py
# def run():
#     r = Report()
#     print(r.getCompleted())
