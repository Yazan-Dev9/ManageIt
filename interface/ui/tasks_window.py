from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QLabel,
    QHBoxLayout,
    QPushButton,
)


class TasksWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.addBtn()
        self.editBtn()
        self.deleteBtn()
        self.btnLayout()
        self.mainLayout()

    def addBtn(self):
        self.add_btn = QPushButton("Add")

    def editBtn(self):
        self.edit_btn = QPushButton("Edit")

    def deleteBtn(self):
        self.delete_btn = QPushButton("Delete")

    def btnLayout(self):
        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.add_btn)
        self.btn_layout.addWidget(self.edit_btn)
        self.btn_layout.addWidget(self.delete_btn)

    def mainLayout(self):
        layout = QVBoxLayout()
        self.list = QListWidget()
        layout.addWidget(QLabel("Tasks List:"))
        layout.addWidget(self.list)
        layout.addLayout(self.btn_layout)
        self.setLayout(layout)
