import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from classes.children.Commission import Commission
from classes.children.Salaried import Salaried


class Root(QMainWindow):

    def __init__(self):
        super().__init__()
        self.data = None

        uic.loadUi("main.ui", self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Root()
    gui.show()

    sys.exit(app.exec_())