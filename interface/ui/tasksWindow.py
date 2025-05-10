from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem,
    QMessageBox,
)
from controllers.taskController import TaskController
from interface.ui.inputTaskWidget import InputTaskWidget


class TasksWindow(QWidget):
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
        self.add_btn.clicked.connect(self.addTask)

    def editBtn(self):
        self.edit_btn = QPushButton("Edit")
        self.edit_btn.clicked.connect(self.editTask)

    def deleteBtn(self):
        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.deleteTask)

    def btnLayout(self):
        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.add_btn)
        self.btn_layout.addWidget(self.edit_btn)
        self.btn_layout.addWidget(self.delete_btn)

    def tableView(self):
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Title", "Description", "Employee Name", "Start", "End", "Status"]
        )
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)

        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setSelectionMode(self.table.SingleSelection)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.row_position = self.table.rowCount()
        self.tasks = TaskController()
        self.putItems()

    def putItems(self):
        self.table.setRowCount(0)
        self.table.setDisabled(False)
        tasks_list = self.tasks.fetchList()
        if tasks_list:
            for task in tasks_list:
                self.table.insertRow(self.row_position)
                self.table.setItem(
                    self.row_position,
                    0,
                    QTableWidgetItem(str(task.getId)),
                )
                self.table.setItem(
                    self.row_position,
                    1,
                    QTableWidgetItem(task.getTitle),
                )
                self.table.setItem(
                    self.row_position,
                    2,
                    QTableWidgetItem(task.getDescription),
                )
                self.table.setItem(
                    self.row_position,
                    3,
                    QTableWidgetItem(task.getEmployee.getName),  # type: ignore
                )
                self.table.setItem(
                    self.row_position,
                    4,
                    QTableWidgetItem(task.getStartDate.isoformat()),  # type: ignore
                )
                self.table.setItem(
                    self.row_position,
                    5,
                    QTableWidgetItem(task.getEndDate.isoformat()),  # type: ignore
                )
                self.table.setItem(
                    self.row_position,
                    6,
                    QTableWidgetItem(task.getStatus),
                )
        else:
            self.table.setDisabled(True)

    def addTask(self):
        window = InputTaskWidget()
        window.exec_()
        self.putItems()

    def deleteTask(self):
        row = self.table.currentRow()
        if row >= 0:
            msg = QMessageBox.question(
                self,
                "Delete",
                "Are you sure you want to delete this task?",
                QMessageBox.Yes | QMessageBox.No,
            )

            if msg == QMessageBox.Yes:
                item = self.table.item(row, 0)
                self.tasks.remove(int(item.text()))
                self.table.removeRow(row)
            else:
                print("Canceled")

    def editTask(self):
        row = self.table.currentRow()
        if row >= 0:
            window = InputTaskWidget(self.table)
            window.exec_()
            self.putItems()

    def mainLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("task List:"))
        layout.addWidget(self.table)
        layout.addLayout(self.btn_layout)
        self.setLayout(layout)
