from PyQt5.QtWidgets import QWidget
from ui.pages.terminal_UI import Ui_Form


class Terminal(QWidget):
    def __init__(self):
        super(Terminal, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
