import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QDesktopWidget

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 400, 200)
        self.center()

        # Set up the layout
        self.layout = QVBoxLayout()

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter your expression here...")
        self.layout.addWidget(self.input_field)

        # Result label
        self.result_label = QLabel("Result: ")
        self.layout.addWidget(self.result_label)

        # Buttons for operations
        self.button_layout = QHBoxLayout()
        self.buttons = {
            'Add': '+',
            'Subtract': '-',
            'Multiply': '*',
            'Divide': '/'
        }
        for label, symbol in self.buttons.items():
            button = QPushButton(label)
            button.clicked.connect(lambda _, s=symbol: self.add_symbol(s))
            self.button_layout.addWidget(button)
        self.layout.addLayout(self.button_layout)

        # Equal button to evaluate the expression
        self.equal_button = QPushButton("=")
        self.equal_button.clicked.connect(self.evaluate_expression)
        self.layout.addWidget(self.equal_button)

        # Set the layout
        self.setLayout(self.layout)

    def center(self):
        """Center the window on the screen."""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_symbol(self, symbol):
        """Append the symbol to the input field."""
        current_text = self.input_field.text()
        self.input_field.setText(current_text + symbol)

    def evaluate_expression(self):
        """Evaluate the expression in the input field and display the result."""
        try:
            expression = self.input_field.text()
            result = eval(expression)
            self.result_label.setText(f"Result: {result}")
        except Exception as e:
            self.result_label.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
