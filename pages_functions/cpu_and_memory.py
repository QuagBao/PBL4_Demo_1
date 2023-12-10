from PyQt5.QtWidgets import QWidget
from ui.pages.cpu_and_memory_UI import Ui_Form


class CPU_and_Memory(QWidget):
    def __init__(self):
        super(CPU_and_Memory, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)