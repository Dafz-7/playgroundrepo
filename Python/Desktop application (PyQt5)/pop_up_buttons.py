import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QDesktopWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Open Pop-up", self)
        self.button.setGeometry(100, 30, 100, 30)
        self.button.clicked.connect(self.open_popup)

    def open_popup(self):
        self.popup = PopupWindow()
        self.popup.exec_()

class PopupWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pop-up Window")
        self.setGeometry(200, 200, 200, 100)
        layout = QVBoxLayout()

        label = QLabel("This is a pop-up window.", self)
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
