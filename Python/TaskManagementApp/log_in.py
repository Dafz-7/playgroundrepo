import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class LoginWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app  # Reference to MainApp

        self.setWindowTitle("Log in - Task Management App")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Title
        self.label_title = QLabel("Log in", self)
        self.label_title.setFont(QFont("Arial", 18, QFont.Bold))
        self.label_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_title)

        # Username Input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        # Password Input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Log in Button
        self.login_button = QPushButton("Log in", self)
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button)

        # Don't have an account? Sign up
        self.signup_label = QLabel("<a href='#'>Don't have an account? Sign up here</a>", self)
        self.signup_label.setAlignment(Qt.AlignCenter)
        self.signup_label.setOpenExternalLinks(False)
        self.signup_label.linkActivated.connect(self.redirect_to_signup)
        layout.addWidget(self.signup_label)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Login Failed", "Please enter both username and password.")
            return

        conn = self.main_app.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nickname FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            QMessageBox.information(self, "Login Successful", f"Welcome, {user[0]}!")
            self.main_app.show_welcome(username)  # Redirect to Welcome Page
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid credentials.")

    def redirect_to_signup(self):
        """Switch to Sign Up page."""
        self.main_app.setCurrentWidget(self.main_app.signup_window)