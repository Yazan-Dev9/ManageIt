import sys
from typing import Optional
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QStackedWidget,
)
from interface.ui.employeesWindow import EmployeesWindow
from interface.ui.reportsWindow import ReportsWindow
from interface.ui.tasksWindow import TasksWindow
from models.user import User


class MainWindow(QMainWindow):
    def __init__(self, user: Optional[User] = None):
        super().__init__()
        self.setWindowTitle("Management Employees And Tasks Software")
        self.resize(800, 600)
        self.user: Optional[User] = user
        self.initUi()

    def initUi(self):
        self.mainMenu()
        self.mainPages()
        self.mainLayout()

    def mainMenu(self):
        self.menu = QListWidget()
        self.menu.addItem("Home")
        self.menu.addItem("Employees")
        self.menu.addItem("Tasks")
        self.menu.addItem("Reports")
        self.menu.setFixedWidth(120)
        self.menu.currentRowChanged.connect(self.display_page)

    def mainPages(self):
        self.pages = QStackedWidget()
        self.home_widget = QLabel(f"Welcome In System : {self.user.getFullName}")  # type: ignore
        self.pages.addWidget(self.home_widget)
        self.employees_widget = EmployeesWindow()
        self.pages.addWidget(self.employees_widget)
        self.tasks_widget = TasksWindow()
        self.pages.addWidget(self.tasks_widget)
        self.reports_widget = ReportsWindow()
        self.pages.addWidget(self.reports_widget)

    def mainLayout(self):
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.menu)
        main_layout.addWidget(self.pages)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        self.menu.setCurrentRow(0)

    def display_page(self, index):
        self.pages.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
