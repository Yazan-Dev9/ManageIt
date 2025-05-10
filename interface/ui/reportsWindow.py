from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


class ReportsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.mainLayout()

    def mainLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Reports Interface:"))
        self.setLayout(layout)
