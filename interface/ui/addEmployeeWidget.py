from PyQt5.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QDialog,
)

from controllers.employeeController import EmployeeController


class AddEmployeeWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employee")
        self.initUi()

    def initUi(self):
        # حقول الإدخال
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()
        self.position_input = QLineEdit()

        # تسميات الحقول
        name_label = QLabel("Name:")
        phone_label = QLabel("Phone:")
        email_label = QLabel("email:")
        position_label = QLabel("position:")

        # زر الإضافة
        add_button = QPushButton("إضافة")
        add_button.clicked.connect(self.add_person)

        # تخطيطات أفقية لكل حقل مع التسمية
        name_layout = QHBoxLayout()
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)

        phone_layout = QHBoxLayout()
        phone_layout.addWidget(phone_label)
        phone_layout.addWidget(self.phone_input)

        email_layout = QHBoxLayout()
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.email_input)

        position_layout = QHBoxLayout()
        position_layout.addWidget(position_label)
        position_layout.addWidget(self.position_input)

        # التخطيط الرئيسي
        main_layout = QVBoxLayout()
        main_layout.addLayout(name_layout)
        main_layout.addLayout(phone_layout)
        main_layout.addLayout(email_layout)
        main_layout.addLayout(position_layout)
        main_layout.addWidget(add_button)

        self.setLayout(main_layout)

    def add_person(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        position = self.position_input.text()

        if not name or not phone or not email or not position:
            QMessageBox.warning(self, "Error", "Please Enter All")
            return
        else:
            if EmployeeController().saveEmployee(name, phone, email, position):
                QMessageBox.information(self, "Added Done", "Employee Added Successfully")
            else:
                QMessageBox.warning(self, "Error", "Employee Not Added")
        self.close()
