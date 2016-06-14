#coding: utf8
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('spl')
form_class, base_class = loadUiType('window.ui')


class MainWindow(QDialog, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        self.setupUi(self)

    #----------------------------------------------------#

    def buttonClick (self):
        self.lineedit.setText("test ok!")

form = MainWindow()
form.setWindowTitle('spl')
form.show()
sys.exit(app.exec_())