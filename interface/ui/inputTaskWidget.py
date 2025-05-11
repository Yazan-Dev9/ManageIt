from typing import Optional
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QDialog,
    QDateEdit,
    QComboBox,
    QTableWidget,
)


from controllers.taskController import TaskController
from controllers.employeeController import EmployeeController


class InputTaskWidget(QDialog):
    def __init__(self, table: Optional[QTableWidget] = None):
        super().__init__()
        self.setWindowIcon(QIcon("./assets/icon/logo.png"))
        self.table = table
        if self.table is None:
            self.setWindowTitle("Add Employee")
        else:
            self.setWindowTitle("Edit Employee")

        self.initUi()
        self.put()

    def initUi(self):
        self.titleInput()
        self.descriptionInput()
        self.employeeInput()
        self.startDateInput()
        self.endDateInput()
        self.statusInput()
        self.titleLabel()
        self.descriptionLabel()
        self.employeeLabel()
        self.startDateLabel()
        self.endDateLabel()
        self.statusLabel()
        self.addBtn()
        self.titleLayout()
        self.descriptionLayout()
        self.employeeLayout()
        self.startDateLayout()
        self.endDateLayout()
        self.statusLayout()
        self.mainLayout()

    def titleInput(self):
        self.title_input = QLineEdit()

    def descriptionInput(self):
        self.description_input = QLineEdit()

    def employeeInput(self):
        self.employee_input = QComboBox()
        self.employee_input.addItem("Select Employee")
        employees = EmployeeController().fetchList()

        for employee in employees:
            self.employee_input.addItem(employee.getName, employee.getId)

    def startDateInput(self):
        self.start_date_input = QDateEdit()
        self.start_date_input.setDisplayFormat("yyyy-MM-dd")

    def endDateInput(self):
        self.end_date_input = QDateEdit()
        self.end_date_input.setDisplayFormat("yyyy-MM-dd")

    def statusInput(self):
        self.status_input = QComboBox()
        self.status_input.addItem("Select Status")
        status_list = ("Completed", "Progress")

        for status in status_list:
            self.status_input.addItem(status)

    def titleLabel(self):
        self.title_label = QLabel("title:")

    def descriptionLabel(self):
        self.description_label = QLabel("description:")

    def employeeLabel(self):
        self.employee_label = QLabel("employee:")

    def startDateLabel(self):
        self.start_date_label = QLabel("start:")

    def endDateLabel(self):
        self.end_date_label = QLabel("end:")

    def statusLabel(self):
        self.status_label = QLabel("status:")

    def put(self):
        if self.table is not None:
            row = self.table.currentRow()
            self.title_input.setText(self.table.item(row, 1).text())
            self.description_input.setText(self.table.item(row, 2).text())
            self.employee_input.setCurrentText(self.table.item(row, 3).text())
            start_str = self.table.item(row, 4).text()
            self.start_date_input.setDate(QDate.fromString(start_str, "yyyy-MM-dd"))
            end_str = self.table.item(row, 5).text()
            self.end_date_input.setDate(QDate.fromString(end_str, "yyyy-MM-dd"))
            self.status_input.setCurrentText(self.table.item(row, 6).text())

    def addBtn(self):
        self.add_button = QPushButton("Save")
        self.add_button.clicked.connect(self.addTask)

    def titleLayout(self):
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.title_input)

    def descriptionLayout(self):
        self.description_layout = QHBoxLayout()
        self.description_layout.addWidget(self.description_label)
        self.description_layout.addWidget(self.description_input)

    def employeeLayout(self):
        self.employee_layout = QHBoxLayout()
        self.employee_layout.addWidget(self.employee_label)
        self.employee_layout.addWidget(self.employee_input)

    def startDateLayout(self):
        self.start_date_layout = QHBoxLayout()
        self.start_date_layout.addWidget(self.start_date_label)
        self.start_date_layout.addWidget(self.start_date_input)

    def endDateLayout(self):
        self.end_date_layout = QHBoxLayout()
        self.end_date_layout.addWidget(self.end_date_label)
        self.end_date_layout.addWidget(self.end_date_input)

    def statusLayout(self):
        self.status_layout = QHBoxLayout()
        self.status_layout.addWidget(self.status_label)
        self.status_layout.addWidget(self.status_input)

    def mainLayout(self):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.title_layout)
        main_layout.addLayout(self.description_layout)
        main_layout.addLayout(self.employee_layout)
        main_layout.addLayout(self.start_date_layout)
        main_layout.addLayout(self.end_date_layout)
        if self.table is not None:
            main_layout.addLayout(self.status_layout)
        main_layout.addWidget(self.add_button)

        self.setLayout(main_layout)

    def addTask(self):
        title = self.title_input.text()
        description = self.description_input.text()
        employee_id = self.employee_input.currentData()
        start_date = self.start_date_input.text()
        end_date = self.end_date_input.text()
        status = self.status_input.currentText()

        if (
            not title
            or not description
            or not employee_id
            or not start_date
            or not end_date
            or not status
        ):
            QMessageBox.warning(self, "Error", "Please Enter All")
            return
        else:
            if self.table is None:
                if TaskController().save(
                    title,
                    description,
                    employee_id,
                    start_date,
                    end_date,
                    self.status_input.itemText(1),
                ):
                    QMessageBox.information(
                        self, "Added Done", "Task Added Successfully"
                    )
                else:
                    QMessageBox.warning(self, "Error", "Task Not Added")

            else:
                if TaskController().edit(
                    int(self.table.item(self.table.currentRow(), 0).text()),
                    title,
                    description,
                    employee_id,
                    start_date,
                    end_date,
                    status,
                ):
                    QMessageBox.information(
                        self, "Updated Done", "Task Updated Successfully"
                    )
                else:
                    QMessageBox.warning(self, "Error", "Task Not Updated")

        self.close()
