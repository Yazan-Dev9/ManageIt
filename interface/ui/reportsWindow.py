from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QHeaderView,
    QHBoxLayout,
    QTableWidgetItem
)
from reports.report import Report


class ReportsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.completedBtn()
        self.progressBtn()
        self.btnLayout()
        self.tableView()
        self.refreshBtn()
        self.mainLayout()

    def completedBtn(self):
        self.completed_btn = QPushButton("Completed")
        self.completed_btn.clicked.connect(self.completedView)

    def progressBtn(self):
        self.progress_btn = QPushButton("Progress")
        self.progress_btn.clicked.connect(self.progressView)

    def tableView(self):
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Employee", "Total Task", "Completed"])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.row_position = self.table.rowCount()
        self.reports = Report()
        self.completedView()
        self.putItems()

    def completedView(self):
        self.table.setHorizontalHeaderLabels(["Employee", "Total Task", "Completed"])
        self.putItems()

    def progressView(self):
        self.table.setHorizontalHeaderLabels(["Employee", "Total Task", "Progress"])
        self.putItems()

    def putItems(self):
        self.table.setRowCount(0)
        self.table.setDisabled(False)
        header_text = self.table.horizontalHeaderItem(2).text()

        if header_text == "Completed":
            self.report_list = self.reports.getCompleted()
        else:
            self.report_list = self.reports.getProgress()

        if self.report_list:
            for report in self.report_list:
                self.table.insertRow(self.row_position)
                self.table.setItem(
                    self.row_position, 0, QTableWidgetItem(str(report[0]))
                )
                self.table.setItem(
                    self.row_position, 1, QTableWidgetItem(str(report[1]))
                )
                self.table.setItem(
                    self.row_position, 2, QTableWidgetItem(str(report[2]))
                )
        else:
            self.table.setDisabled(True)

    def refreshBtn(self):
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.putItems)

    def btnLayout(self):
        self.btn_layout = QHBoxLayout()
        self.btn_layout.addWidget(self.completed_btn)
        self.btn_layout.addWidget(self.progress_btn)

    def mainLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Reports Interface:"))
        layout.addLayout(self.btn_layout)
        layout.addWidget(self.table)
        layout.addWidget(self.refresh_btn)

        self.setLayout(layout)
