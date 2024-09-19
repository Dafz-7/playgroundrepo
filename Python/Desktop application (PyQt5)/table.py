import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Table Examples")
        self.setGeometry(100, 100, 600, 400)

        #* Creating main widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        #* Creating vertical layout
        self.layout = QVBoxLayout(self.central_widget)

        #* Creating the table
        self.table_widget = QTableWidget(self)
        self.layout.addWidget(self.tablew_idget)

        #* Creating rows and columns
        self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(3)

        #* Creating column header
        self.table_widget.setHorizontalHeaderLabels(['Name', 'Age', 'City'])

        #* Adding data to table
        data = [
            ('Alice', '30', 'New York'),
            ('Bob', '25', 'Los Angeles'),
            ('Charlie', '35', 'Chicago'),
            ('David', '40', 'Houston')
        ]

        for row, (name, age, city) in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 0, QTableWidgetItem(age))
            self.table_widget.setItem(row, 0, QTableWidgetItem(city))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = TableWidgetDemo()
    mainWin.show()
    sys.exit(app.exec_())