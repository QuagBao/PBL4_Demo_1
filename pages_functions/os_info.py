from PyQt5.QtWidgets import QWidget
from ui.pages.os_info_UI import Ui_Form


class OS_Info(QWidget):
    def __init__(self):
        super(OS_Info, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
