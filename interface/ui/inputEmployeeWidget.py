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


class InputEmployeeWidget(QDialog):
    def __init__(self, table=None):
        super().__init__()
        self.table = table
        if self.table is None:
            self.setWindowTitle("Add Employee")
        else:
            self.setWindowTitle("Edit Employee")

        self.initUi()
        self.put()

    def initUi(self):
        self.nameInput()
        self.phoneInput()
        self.emailInput()
        self.positionInput()
        self.nameLabel()
        self.phoneLabel()
        self.emailLabel()
        self.positionLabel()
        self.addBtn()
        self.nameLayout()
        self.phoneLayout()
        self.emailLayout()
        self.positionLayout()
        self.mainLayout()

    def nameInput(self):
        self.name_input = QLineEdit()

    def phoneInput(self):
        self.phone_input = QLineEdit()

    def emailInput(self):
        self.email_input = QLineEdit()

    def positionInput(self):
        self.position_input = QLineEdit()

    def nameLabel(self):
        self.name_label = QLabel("Name:")

    def phoneLabel(self):
        self.phone_label = QLabel("Phone:")

    def emailLabel(self):
        self.email_label = QLabel("email:")

    def positionLabel(self):
        self.position_label = QLabel("position:")

    def addBtn(self):
        self.add_button = QPushButton("Save")
        self.add_button.clicked.connect(self.add_person)

    def nameLayout(self):
        self.name_layout = QHBoxLayout()
        self.name_layout.addWidget(self.name_label)
        self.name_layout.addWidget(self.name_input)

    def phoneLayout(self):
        self.phone_layout = QHBoxLayout()
        self.phone_layout.addWidget(self.phone_label)
        self.phone_layout.addWidget(self.phone_input)

    def emailLayout(self):
        self.email_layout = QHBoxLayout()
        self.email_layout.addWidget(self.email_label)
        self.email_layout.addWidget(self.email_input)

    def positionLayout(self):
        self.position_layout = QHBoxLayout()
        self.position_layout.addWidget(self.position_label)
        self.position_layout.addWidget(self.position_input)

    def mainLayout(self):
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.name_layout)
        main_layout.addLayout(self.phone_layout)
        main_layout.addLayout(self.email_layout)
        main_layout.addLayout(self.position_layout)
        main_layout.addWidget(self.add_button)

        self.setLayout(main_layout)

    def put(self):
        if self.table is not None:
            self.name_input.setText(self.table.item(0, 1).text())
            self.phone_input.setText(self.table.item(0, 2).text())
            self.email_input.setText(self.table.item(0, 3).text())
            self.position_input.setText(self.table.item(0, 4).text())

    def add_person(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        position = self.position_input.text()

        if not name or not phone or not email or not position:
            QMessageBox.warning(self, "Error", "Please Enter All")
            return
        else:
            if self.table is None:
                if EmployeeController().save(name, phone, email, position):
                    QMessageBox.information(
                        self, "Added Done", "Employee Added Successfully"
                    )
                else:
                    QMessageBox.warning(self, "Error", "Employee Not Added")

            else:
                if EmployeeController().edit(
                    self.table.item(self.table.currentRow(), 0).text(),
                    name,
                    phone,
                    email,
                    position,
                ):
                    QMessageBox.information(
                        self, "Updated Done", "Employee Updated Successfully"
                    )
                else:
                    QMessageBox.warning(self, "Error", "Employee Not Updated")

        self.close()
