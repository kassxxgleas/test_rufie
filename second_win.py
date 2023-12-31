# код основної програми та другого екрану
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from second_win import *

class Main_win (QWidget):
    def __init__(self):
        super().__init__
        self.initUi()
        self.connects()
        self.setAppear()
        self.show()
