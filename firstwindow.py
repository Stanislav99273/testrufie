from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit
from instr import *
from secondWindow import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connect()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.lb_hello = QLabel(txt_hello)
        self.lb_instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)

        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.lb_instruction, alignment= Qt.AlignCenter)
        self.v_line.addWidget(self.lb_hello, alignment= Qt.AlignCenter)
        self.v_line.addWidget(self.btn_next, alignment= Qt.AlignCenter)

        self.setLayout(self.v_line)
       
    def connect (self):
        self.btn_next.clicked.connect(self.next_window)

    def next_window(self):
        self.hide()
        self.sec_win = SecondWindow()



app = QApplication([])
mainWindow = MainWindow()
app.exec_()