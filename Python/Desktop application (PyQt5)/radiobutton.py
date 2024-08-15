from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup, QDesktopWidget

#* Create application object
app = QApplication([])

#* Setting up window positions
my_win = QWidget()
my_win.setWindowTitle("Radio buttons")
my_win.resize(400, 200)

def center():
    qr = my_win.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    my_win.move(qr.topLeft())

center()

my_win.show()

#* Creating vertical layout
line = QVBoxLayout()

#* Setting up radio button objects
radiobutton1 = QRadioButton("1")
radiobutton1.setChecked(True)
radiobutton2 = QRadioButton("2")
radiobutton3 = QRadioButton("3")

#* Setting up button group objects
button_group = QButtonGroup()
button_group.addButton(radiobutton1, id = 1)
button_group.addButton(radiobutton2, id = 2)
button_group.addButton(radiobutton3, id = 3)

#* Setting radio buttons on the layout
line.addWidget(radiobutton1)
line.addWidget(radiobutton2)
line.addWidget(radiobutton3)

#* Creating a button with a label and positioning
button = QPushButton("Check")
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)

#* Creating resulted text when a radio button is pressed
title = QLabel()
line.addWidget(title, alignment = Qt.AlignCenter)
my_win.setLayout(line)

#* Creating a function for other radio buttons
def radio_button_check():
    title.setText("Selected: Button number " + str(button_group.checkedId()))

#* Check for button presses
button.clicked.connect(radio_button_check)

#* Run the app
app.exec_()
