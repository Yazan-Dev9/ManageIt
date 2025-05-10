from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView
)

from controllers.employeeController import EmployeeController
from interface.ui.inputEmployeeWidget import InputEmployeeWidget


class EmployeesWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.addBtn()
        self.editBtn()
        self.deleteBtn()
        self.tableView()
        self.btnLayout()
        self.mainLayout()

    def addBtn(self):
        self.add_btn = QPushButton("Add")
        self.add_btn.clicked.connect(self.addEmployee)

    def editBtn(self):
        self.edit_btn = QPushButton("Edit")
        self.edit_btn.clicked.connect(self.editEmployee)

    def deleteBtn(self):
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.deleteEmployee)

    def btnLayout(self):
        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.add_btn)
        self.btn_layout.addWidget(self.edit_btn)
        self.btn_layout.addWidget(self.delete_btn)

    def tableView(self):
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Name", "Email", "Phone", "Position"]
        )
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)

        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setSelectionMode(self.table.SingleSelection)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.row_position = self.table.rowCount()
        self.employees = EmployeeController()
        self.putItems()

    def putItems(self):
        self.table.setRowCount(0)
        self.table.setDisabled(False)
        employees_list = self.employees.fetchList()
        if employees_list:
            for employee in employees_list:
                self.table.insertRow(self.row_position)
                self.table.setItem(
                    self.row_position, 0, QTableWidgetItem(str(employee.getId))
                )
                self.table.setItem(
                    self.row_position, 1, QTableWidgetItem(employee.getName)
                )
                self.table.setItem(
                    self.row_position, 2, QTableWidgetItem(employee.getEmail)
                )
                self.table.setItem(
                    self.row_position, 3, QTableWidgetItem(employee.getPhone)
                )
                self.table.setItem(
                    self.row_position, 4, QTableWidgetItem(employee.getPosition)
                )
        else:
            self.table.setDisabled(True)

    def addEmployee(self):
        window = InputEmployeeWidget()
        window.exec_()
        self.putItems()

    def deleteEmployee(self):
        row = self.table.currentRow()
        if row >= 0:
            msg = QMessageBox.question(
                self,
                "Delete",
                "Are you sure you want to delete this employee?",
                QMessageBox.Yes | QMessageBox.No,
            )

            if msg == QMessageBox.Yes:
                item = self.table.item(row, 0)
                self.employees.remove(int(item.text()))
                self.table.removeRow(row)
            else:
                print("Canceled")

    def editEmployee(self):
        row = self.table.currentRow()
        if row >= 0:
            window = InputEmployeeWidget(self.table)
            window.exec_()
            self.putItems()

    def mainLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Employees List:"))
        layout.addWidget(self.table)
        layout.addLayout(self.btn_layout)
        self.setLayout(layout)
