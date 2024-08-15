import sys
import random
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDesktopWidget

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

        # Create QTimer and connect to update_timer function
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Random stop time between 5 to 15 seconds
        self.stop_time = random.randint(5, 15)
        self.elapsed_time = 0

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def init_ui(self):
        self.setWindowTitle("A Simple Random-Ending Timer")

        layout = QVBoxLayout()

        # Label to display elapsed time
        self.label = QLabel("Elapsed time: 0", self)
        layout.addWidget(self.label)

        # Button to start the timer
        self.start_button = QPushButton("Start timer", self)
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

        # Center the window
        self.center()

    def start_timer(self):
        # Set timer interval to 1000ms (1 second)
        self.timer.start(1000)
        self.elapsed_time = 0

    def update_timer(self):
        # Increment elapsed time
        self.elapsed_time += 1
        self.label.setText(f"Elapsed Time: {self.elapsed_time}")

        # Stop timer if stop time is reached
        if self.elapsed_time >= self.stop_time:
            self.timer.stop()
            self.label.setText(f"Timer stopped at {self.elapsed_time} seconds!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TimerApp()
    ex.show()
    sys.exit(app.exec_())