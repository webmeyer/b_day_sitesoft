from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500, 500, 500, 300)
        self.setWindowTitle('Happy B-Day sender for Sitesoft')
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Test label')
        self.label.move(50, 50)

        self.bl = QtWidgets.QPushButton(self)
        self.bl.setText('CLICK ME!')
        self.bl.move(150, 150)
        self.bl.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('U pressed the button')
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()


    win.show()
    sys.exit(app.exec())

window()