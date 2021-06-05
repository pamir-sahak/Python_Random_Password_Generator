from password import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import sys
import random


# generates random lowercase password from a to z
def generate_lowercase_password(length):
    password = ""
    for i in range(length):
        letter = random.randint(97, 122)
        password += chr(letter)

    return password


# generates random lowercase + Uppercase password from A-Z to a-z
def generate_uppercase_password(length):
    list = []
    password = ""
    for i in range(int(length / 2)):
        letter = random.randint(65, 90)
        letter2 = random.randint(65, 90)
        list.append(chr(letter))
        list.append(chr(letter2).lower())

    random.shuffle(list)

    for i in list:
        password += i

    return password


# generates random password mixed with A-Z, a-z and special characters
def generate_password_with_special_chars(length):
    password = ""
    for i in range(length):
        letter = random.randint(33, 126)

        password += chr(letter)

    return password


# generates random password mixed with A-Z, a-z and special characters
def generate_password_with_special_chars_lower(length):
    list = []
    password = ""
    for i in range(int(length / 2)):
        letter = random.randint(33, 63)
        letter2 = random.randint(65, 90)
        list.append(chr(letter))
        list.append(chr(letter2).lower())

    random.shuffle(list)

    for i in list:
        password += i

    return password


class Window(QtWidgets.QMainWindow):
    password = ""

    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnGenerate.clicked.connect(self.generate_password)
        self.ui.btn_add_lenght.clicked.connect(self.add_length)
        self.ui.btn_minus_lenght.clicked.connect(self.minus_length)

        self.setWindowTitle("Random Password Generator")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

    # generates password according to user choices
    def generate_password(self):
        # generates uppercase + lowercase + special characters password
        if self.ui.special_chars_cbox.isChecked() and self.ui.uppercase_cbox.isChecked():
            self.password = generate_password_with_special_chars(int(self.ui.lbl_lenght.text()))
            self.ui.lbl_password.setText(self.password)

        # generates uppercase + lowercase
        elif self.ui.uppercase_cbox.isChecked():
            self.password = generate_uppercase_password(int(self.ui.lbl_lenght.text()))
            self.ui.lbl_password.setText(self.password)

        # generates lowercase + special characters password
        elif self.ui.special_chars_cbox.isChecked():
            self.password = generate_password_with_special_chars_lower(int(self.ui.lbl_lenght.text()))
            self.ui.lbl_password.setText(self.password)

        # generates only lowercase password
        else:
            self.password = generate_lowercase_password(int(self.ui.lbl_lenght.text()))
            self.ui.lbl_password.setText(self.password)

    # making length plus one when button clicked
    def add_length(self):
        length = int(self.ui.lbl_lenght.text())
        length += 1
        self.ui.lbl_lenght.setText(str(length))

    # making length minus one when button clicked
    def minus_length(self):
        length = int(self.ui.lbl_lenght.text())
        if length > 1:
            length -= 1
            self.ui.lbl_lenght.setText(str(length))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Length Error")

            msg.setFixedSize(400, 200)
            msg.setText("Length can not be zero or smaller than zero")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowIcon(QtGui.QIcon("icon/qr.png"))

            x = msg.exec_()


# making an instance of the window and running the program
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


app()
