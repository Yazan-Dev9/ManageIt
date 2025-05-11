import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
)
from interface.ui.mainWindow import MainWindow
from controllers.authController import AuthController


class RegisterPage(QWidget):
    TITLE = "Register Page"

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./assets/icon/logo.png"))
        self.setWindowTitle(RegisterPage.TITLE)
        self.initUi()

    def initUi(self):
        self.header()
        self.fullName()
        self.userName()
        self.password()
        self.confirmPassword()
        self.checkAdmin()
        self.registerBtn()
        self.mainLayout()

    def header(self):
        self.header_label = QLabel("Register Page")
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def userName(self):
        self.username_label = QLabel("UserName:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        self.username_layout = QHBoxLayout()
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_input)

    def password(self):
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.password_layout = QHBoxLayout()
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)

    def confirmPassword(self):
        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Enter your password again")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_layout = QHBoxLayout()
        self.confirm_password_layout.addWidget(self.confirm_password_label)
        self.confirm_password_layout.addWidget(self.confirm_password_input)

    def fullName(self):
        self.name_label = QLabel("Full Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your full name")

        self.name_layout = QHBoxLayout()
        self.name_layout.addWidget(self.name_label)
        self.name_layout.addWidget(self.name_input)

    def checkAdmin(self):
        self.check_admin = QCheckBox()
        self.check_admin.setText("Admin")

    def registerBtn(self):
        self.register_btn = QPushButton("Register")
        self.register_btn.clicked.connect(self.addUser)

    def addUser(self):
        full_name = self.name_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        auth = AuthController()

        if password != confirm_password:
            print("Password and confirm password do not match.")
            return
        admin = self.check_admin.isChecked()
        if admin:
            role = auth.fetchRole("Admin")
        else:
            role = auth.fetchRole("Member")

        if auth.save(username, password, full_name, role.getId):  # type: ignore
            print("User added successfully.")
            auth.fetch(username)
            self.main_window = MainWindow(auth.getUser)
            self.main_window.show()
            self.close()

    def mainLayout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.header_label)
        main_layout.addLayout(self.name_layout)
        main_layout.addLayout(self.username_layout)
        main_layout.addLayout(self.password_layout)
        main_layout.addLayout(self.confirm_password_layout)
        main_layout.addWidget(self.check_admin)
        main_layout.addWidget(self.register_btn)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterPage()
    window.show()
    app.exec_()
