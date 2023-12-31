# код основної програми та першого екрану
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from second_win import *

class Main_win (QWidget):
    def __init__(self):
        super().__init__
        self.initUi()
        #self.connects()
        self.setAppear()
        #self.show()

    def initUi(self):
        self.button_next = QPushButton(txt_next,self)
        self.hello_text = QLabel(text_hello)
        self.intr = QLabel(txt_instructions)
        self.layout_1 = QVBoxLayout()
        self.layout_1.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout_1.addWidget(self.intr, alignment=Qt.AlignLeft)
        self.layout_1.addWidget(self.button_next,alignment=Qt.AlignCenter)       
        self.setLayout(self.layout_1)

    def setAppear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)

    def connects(self):
        self.button_next.clicked.connect(self.next_click)
        
    def next_click(self):
        self.hide()
        #self.second_win = Test_Win()

    









        app = QApplication([])
        window = Main_win()
        app.exec()
