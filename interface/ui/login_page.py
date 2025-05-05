import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QToolButton,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)
from controllers.auth_controller import AuthController


class LoginPage(QWidget):
    WIDTH = 350
    HIGHER = 300
    TITLE = "Login Page"
    CSS_FILE = "./interface/ui/login.css"

    def __init__(self):
        super().__init__()
        self.setWindowTitle(LoginPage.TITLE)
        self.setFixedSize(LoginPage.WIDTH, LoginPage.HIGHER)
        try:
            with open(LoginPage.CSS_FILE, "r") as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError as e:
            print(e, "File not found")

        self.initUi()

    def initUi(self):
        self.header()
        self.userName()
        self.password()
        self.btnEye()
        self.error()
        self.btnLogin()
        self.btnRegister()
        self.passwordLayout()
        self.formLayout()
        self.btnLayout()
        self.mainLayout()

        self.user_input.returnPressed.connect(self.pass_input.setFocus)
        self.pass_input.returnPressed.connect(self.login_btn.setFocus)

    def header(self):
        id = "header_label"
        text = "Welcome! Please Login"

        self.header_label = QLabel()
        self.header_label.setObjectName(id)
        self.header_label.setText(text)
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def userName(self):
        label_id = "user_label"
        input_id = "user_input"
        text = "Username:"
        place_holder = "Enter username"

        self.user_label = QLabel()
        self.user_label.setObjectName(label_id)
        self.user_label.setText(text)

        self.user_input = QLineEdit()
        self.user_input.setObjectName(input_id)
        self.user_input.setPlaceholderText(place_holder)
        self.user_input.setMaxLength(10)

    def password(self):
        label_id = "pass_label"
        input_id = "pass_input"
        text = "Password:"
        place_holder = "Enter password"

        self.pass_label = QLabel()
        self.pass_label.setObjectName(label_id)
        self.pass_label.setText(text)

        self.pass_input = QLineEdit()
        self.pass_input.setObjectName(input_id)
        self.pass_input.setPlaceholderText(place_holder)
        self.pass_input.setEchoMode(QLineEdit.Password)

    def btnEye(self):
        id = "eye_btn"

        self.eye_btn = QToolButton()
        self.eye_btn.setObjectName(id)
        self.eye_btn.setText("👁️")
        self.eye_btn.setCheckable(True)
        self.eye_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.eye_btn.setToolTip("Show/Hide password")
        self.eye_btn.setContentsMargins(0, -25, 0, 0)
        self.eye_btn.clicked.connect(self.toggle_password)

    def error(self):
        id = "massage_label"

        self.massage_label = QLabel()
        self.massage_label.setText("Alert Error Massage")
        self.massage_label.hide()
        self.massage_label.setObjectName(id)
        self.massage_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def btnLogin(self):
        id = "login_btn"
        text = "Login"

        self.login_btn = QPushButton()
        self.login_btn.setObjectName(id)
        self.login_btn.setText(text)
        self.login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_btn.clicked.connect(self.login_action)

    def btnRegister(self):
        id = "register_btn"
        text = "Register"

        self.register_btn = QPushButton()
        self.register_btn.setObjectName(id)
        self.register_btn.setText(text)
        self.register_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.register_btn.clicked.connect(self.register_action)

    def passwordLayout(self):
        self.pass_layout = QHBoxLayout()
        self.pass_layout.addWidget(self.pass_input)
        self.pass_layout.addWidget(self.eye_btn)

    def formLayout(self):
        self.form_layout = QVBoxLayout()
        self.form_layout.addWidget(self.user_label)
        self.form_layout.addWidget(self.user_input)
        self.form_layout.addWidget(self.pass_label)
        self.form_layout.addLayout(self.pass_layout)

    def btnLayout(self):
        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.login_btn)
        self.btn_layout.addWidget(self.register_btn)

    def mainLayout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.header_label)
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(self.massage_label)
        main_layout.addLayout(self.btn_layout)

        self.setLayout(main_layout)

    def login_action(self):
        username = self.user_input.text()
        password = self.pass_input.text()
        if AuthController.checkUser(username, password):
            self.massage_label.setText("Login Done")
            self.massage_label.show()
            print("Find user Login Done")
        else:
            self.massage_label.setText("Filed to Login")
            self.massage_label.setStyleSheet("color: red;")
            self.massage_label.show()
            print("Filed user Error")

    def register_action(self):
        print("Go to registration page.")

    def toggle_password(self):
        if self.eye_btn.isChecked():
            self.pass_input.setEchoMode(QLineEdit.Normal)
            self.eye_btn.setText("🙈")
        else:
            self.pass_input.setEchoMode(QLineEdit.Password)
            self.eye_btn.setText("👁️")


def start():
    app = QApplication(sys.argv)
    login = LoginPage()
    login.show()
    sys.exit(app.exec_())
