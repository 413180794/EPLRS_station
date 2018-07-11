import os

import sys

from PyQt5.QtCore import  pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog

sys.path.append(os.path.abspath("../Bean"))
from systemInfoWindows import Ui_Dialog

class SystemInfoDialog(QDialog, Ui_Dialog):

    def __init__(self, MainForm=None):
        super(SystemInfoDialog, self).__init__()
        self.setupUi(self)
        self.MainForm = MainForm

    @pyqtSlot()
    def on_close_button_clicked(self):
        self.close()


