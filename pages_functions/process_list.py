from PyQt5.QtWidgets import QWidget
from ui.pages.process_list_UI import Ui_Form


class Process_List(QWidget):
    def __init__(self):
        super(Process_List, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)