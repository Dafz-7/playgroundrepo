import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QHBoxLayout, QTimeEdit, QDesktopWidget
from PyQt5.QtCore import QTimer, QTime, Qt


#! Main window class
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #* Setting up the UI
        self.init_ui()

    def init_ui(self):
        #* Setting the window title
        self.setWindowTitle("Main menu")
        self.resize(400, 200)

        #* Creating the main layout
        layout = QVBoxLayout()

        #* Creating buttons for the options
        calc_button = QPushButton("Calculator")
        todo_button = QPushButton("To-Do List")
        timer_button = QPushButton("Timer")

        #* Connecting buttons to functions
        calc_button.clicked.connect(self.open_calculator)
        todo_button.clicked.connect(self.open_todo_list)
        timer_button.clicked.connect(self.open_timer)

        #* Adding buttons to the layout
        layout.addWidget(calc_button)
        layout.addWidget(todo_button)
        layout.addWidget(timer_button)
        
        #* Setting the layout to the main window
        self.setLayout(layout)

        #* Centering the window
        self.center()

        #* Showing the window
        self.show()

    #! Center the window function
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_calculator(self):
        self.calculator_window = CalculatorWindow()
        self.calculator_window.show()

    def open_todo_list(self):
        self.todo_list_window = ToDoListWindow()
        self.todo_list_window.show()

    def open_timer(self):
        self.timer_window = TimerWindow()
        self.timer_window.show()


#! Calculator window class
class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__() 

        #* Setting up the UI
        self.init_ui()

    def init_ui(self):
        #* Setting up the window title
        self.setWindowTitle("Calculator")

        #* Creating the main layout
        layout = QVBoxLayout()

        #* Creating display field for the calculator
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(35)
        layout.addWidget(self.display)

        #* Defining buttons
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '(',
            '1', '2', '3', '-', ')',
            '0', '.', '=', '+', 'CE'
        ]

        #* Creating a grid layout for buttons
        grid_layout = QVBoxLayout()

        #* Creating button instances and add them to the layout
        for i in range(0, len(buttons), 5):
            row_layout = QHBoxLayout()
            for j in range(5):
                button = QPushButton(buttons[i + j])
                button.clicked.connect(self.on_button_clicked)
                row_layout.addWidget(button)
            grid_layout.addLayout(row_layout)

        layout.addLayout(grid_layout)

        #* Setting the layout to the calculator window
        self.setLayout(layout)

        #* Centering the window
        self.center()

    def center(self):
        #* Centering the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_button_clicked(self):
        button_text = self.sender().text()

        if button_text == "=":
            try:
                expression = self.display.text()
                result = str(eval(expression))
                self.display.setText(result)
            except:
                self.display.setText("Error")
        elif button_text == "C":
            self.display.clear()
        elif button_text == "CE":
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        else:
            self.display.setText(self.display.text() + button_text)


#! To-Do List Window Class
class ToDoListWindow(QWidget):
    def __init__(self):
        super().__init__()

        #* Setting up the UI
        self.init_ui()

    def init_ui(self):
        #* Setting the window title
        self.setWindowTitle("To-Do List")

        #* Creating the main layout
        layout = QVBoxLayout()

        #* Creating a list widget to display tasks
        self.task_list = QListWidget()

        #* Creating input field for new tasks
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")

        #* Creating buttons to add and remove tasks
        add_task_button = QPushButton("Add Task")
        remove_task_button = QPushButton("Remove Selected Task")

        #* Connecting buttons to functions
        add_task_button.clicked.connect(self.add_task)
        remove_task_button.clicked.connect(self.remove_task)

        #* Adding widgets to the layout
        layout.addWidget(self.task_list)
        layout.addWidget(self.task_input)
        layout.addWidget(add_task_button)
        layout.addWidget(remove_task_button)

        #* Setting the layout to the to-do list window
        self.setLayout(layout)

        #* Centering the window
        self.center()

    def center(self):
        #* Centering the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_task(self):
        task = self.task_input.text()
        if task != "":
            self.task_list.addItem(task)
            self.task_input.clear()

    def remove_task(self):
        list_items = self.task_list.selectedItems()
        if not list_items:
            return
        for item in list_items:
            self.task_list.takeItem(self.task_list.row(item))


#! Creating Timer Window Class
class TimerWindow(QWidget):
    def __init__(self):
        super().__init__()

        #* Setting up the UI
        self.init_ui()

    def init_ui(self):
        #* Setting the window title
        self.setWindowTitle("Timer")

        #* Creating the main layout
        layout = QVBoxLayout()

        #* Creating a QTimeEdit widget to set the time
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("hh:mm:ss.zzz")
        layout.addWidget(self.time_edit)

        #* Creating a label to display the timer
        self.timer_label = QLabel("00:00:00:000")
        self.timer_label.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.timer_label)

        #* Creating a button to start the timer
        self.start_button = QPushButton("Start Timer")
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        #* Creating a button to reset the timer
        self.reset_button = QPushButton("Reset Timer")
        self.reset_button.clicked.connect(self.reset_timer)
        layout.addWidget(self.reset_button)

        #* Create a QTimer to update the time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        #* Setting the layout to the timer window
        self.setLayout(layout)

        #* Centering the window
        self.center()

    def center(self):
        #* Centering the window on the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_button.setText("Start Timer")
        else: 
            self.timer.start(1) #* Updates every millisecond
            self.start_button.setText("Stop Timer")
    
    def reset_timer(self):
        self.timer.stop()
        self.start_button.setText("Start Timer")
        self.timer_label.setText("00:00:00:000")
        self.time_edit.setTime(QTime(0, 0, 0, 0))

    def update_timer(self):
        current_time = self.time_edit.time()
        self.time_edit.setTime(current_time.addMSecs(1))
        self.timer_label.setText(self.time_edit.time().toString("hh:mm:ss.zzz"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
