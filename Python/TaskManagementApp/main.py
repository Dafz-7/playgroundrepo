import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QStackedWidget
from log_in import LoginWindow
from sign_up import SignUpWindow
from welcome import WelcomePage
from scheduling import TaskScheduler

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Create instances of windows
        self.login_window = LoginWindow(self)
        self.signup_window = SignUpWindow(self)
        self.welcome_page = None
        self.scheduling_page = None

        # Add windows to the stacked widget
        self.addWidget(self.login_window)
        self.addWidget(self.signup_window)

        # Start with login window
        self.setCurrentWidget(self.login_window)

    def connect_db(self):
        """Database connection function accessible by all windows."""
        return mysql.connector.connect(
            host="localhost",
            user="tmastorage",  
            password="jonggol",  
            database="TaskManagementApp"
        )

    def show_signup(self):
        """Show the sign-up page."""
        self.setCurrentWidget(self.signup_window)

    def show_welcome(self, username):
        """Show the welcome page after login."""
        self.welcome_page = WelcomePage(username, self)
        self.addWidget(self.welcome_page)
        self.setCurrentWidget(self.welcome_page)

    def show_scheduling(self, user_id, nickname):
        """Show the task scheduling page after login."""
        self.scheduling_page = TaskScheduler(user_id, nickname)
        self.addWidget(self.scheduling_page)
        self.setCurrentWidget(self.scheduling_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())