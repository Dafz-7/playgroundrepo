import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from scheduling import TaskScheduler
from db_connection import connect_db

class WelcomePage(QWidget):
    def __init__(self, username, main_app):
        super().__init__()
        self.username = username
        self.main_app = main_app
        self.user_id, self.nickname = self.get_user_info()

        self.setWindowTitle("Welcome - Task Management App")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Welcome Label
        self.label_welcome = QLabel(f"Welcome, {self.nickname}", self)
        self.label_welcome.setFont(QFont("Arial", 18, QFont.Bold))
        self.label_welcome.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_welcome)

        # Task Scheduling Button
        self.btn_task_scheduling = QPushButton("Go to task scheduling", self)
        self.btn_task_scheduling.clicked.connect(self.go_to_task_scheduling)
        layout.addWidget(self.btn_task_scheduling)

        # Save Data Button
        self.btn_save_data = QPushButton("Save data", self)
        self.btn_save_data.clicked.connect(self.save_data)
        layout.addWidget(self.btn_save_data)

        self.setLayout(layout)

    def get_user_info(self):
        """Retrieve user ID and nickname from the database."""
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nickname FROM users WHERE username = %s", (self.username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return result[0], result[1]  # (user_id, nickname)
        return None, "User"

    def go_to_task_scheduling(self):
        """Navigate to the Task Scheduling page."""
        if self.user_id:
            self.task_scheduling_page = TaskScheduler(self.user_id, self.nickname)
            self.task_scheduling_page.show()
            self.close()  # Close the welcome page

    def save_data(self):
        """Save user task data from Task Scheduling to the database."""
        conn = connect_db()
        cursor = conn.cursor()

        # Retrieve current tasks
        cursor.execute("SELECT task_name, deadline, priority, occurrence FROM tasks WHERE user_id = %s", (self.user_id,))
        tasks = cursor.fetchall()

        if not tasks:
            QMessageBox.warning(self, "Save Failed", "No tasks to save.")
            return

        # Commit and close
        conn.commit()
        conn.close()
        
        QMessageBox.information(self, "Success", "All tasks have been saved successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomePage("example_username", None)  # Replace with actual username from login
    window.show()
    sys.exit(app.exec_())