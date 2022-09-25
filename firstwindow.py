from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QtWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from instr import *

class MainWindow(QWidget):
    def __init__(seft):
        super().__init__()
        self.show()



app = QApplication([])
mainWindow = MainWindow()
app.exec_()