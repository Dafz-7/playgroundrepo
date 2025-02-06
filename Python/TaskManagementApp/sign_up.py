import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class SignUpWindow(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app  # Reference to MainApp

        self.setWindowTitle("Sign Up - Task Management App")
        self.setGeometry(100, 100, 400, 350)

        layout = QVBoxLayout()

        # Title Label
        self.label_title = QLabel("Sign Up", self)
        self.label_title.setFont(QFont("Arial", 18, QFont.Bold))
        self.label_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_title)

        # Username Input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter your username")
        layout.addWidget(self.username_input)

        # Password Input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Confirm Password Input
        self.password_confirm = QLineEdit(self)
        self.password_confirm.setPlaceholderText("Re-type password")
        self.password_confirm.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_confirm)

        # Nickname Input
        self.nickname_input = QLineEdit(self)
        self.nickname_input.setPlaceholderText("What should we call you?")
        layout.addWidget(self.nickname_input)

        # Sign-Up Button
        self.sign_up_button = QPushButton("Sign Up", self)
        self.sign_up_button.clicked.connect(self.sign_up)
        layout.addWidget(self.sign_up_button)

        # Already have an account? Go to Login
        self.login_label = QLabel("<a href='#'>Already have an account? Log in here</a>", self)
        self.login_label.setAlignment(Qt.AlignCenter)
        self.login_label.setOpenExternalLinks(False)
        self.login_label.linkActivated.connect(self.redirect_to_login)
        layout.addWidget(self.login_label)

        self.setLayout(layout)

    def sign_up(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.password_confirm.text()
        nickname = self.nickname_input.text()

        if not username or not password or not confirm_password or not nickname:
            QMessageBox.warning(self, "Sign-Up Failed", "All fields are required.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Sign-Up Failed", "Passwords do not match.")
            return

        conn = self.main_app.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, nickname) VALUES (%s, %s, %s)",
                           (username, password, nickname))
            conn.commit()
            QMessageBox.information(self, "Success", "Account created successfully! Please log in.")
            self.redirect_to_login()  # Redirect to Log In page
        except Exception as err:
            QMessageBox.warning(self, "Error", f"Could not create account: {err}")
        finally:
            cursor.close()
            conn.close()

    def redirect_to_login(self):
        """Switch back to Log In page after signing up."""
        self.main_app.setCurrentWidget(self.main_app.login_window)