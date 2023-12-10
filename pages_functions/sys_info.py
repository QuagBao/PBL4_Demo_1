from PyQt5.QtWidgets import QWidget
from ui.pages.sys_info_UI import Ui_Form


class System_Information(QWidget):
    def __init__(self):
        super(System_Information, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)