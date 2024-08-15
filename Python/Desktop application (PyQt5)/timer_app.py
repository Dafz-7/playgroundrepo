from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import QTimer, QTime
import sys

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        #* Initialize timer and time
        self.timer = QTimer()
        self.time = QTime(0, 0)

        #* Set up the UI
        self.init_ui()

        #* Connect the timer's timeout signal to the update method
        self.timer.timeout.connect(self.update_time)

    def init_ui(self):
        #* Create a label to display the timer
        self.label = QLabel("00:00:00", self)
        self.label.setStyleSheet("font-size: 24px;")

        #* Create a button to start/stop the timer
        self.button = QPushButton("Start timer", self)
        self.button.clicked.connect(self.toggle_timer)

        #* Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        #* Set up the main window
        self.setWindowTitle("A Simple PyQt Timer")
        self.resize(300, 150)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def toggle_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText("Start Timer")
        else:
            self.timer.start(1000) #* timer interval in miliseconds
            self.button.setText("Stop timer")

    def update_time(self):
        self.time = self.time.addSecs(1)
        self.label.setText(self.time.toString("hh:mm:ss"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TimerApp()
    sys.exit(app.exec_())