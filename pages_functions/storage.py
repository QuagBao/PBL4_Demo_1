from PyQt5.QtWidgets import QWidget
from ui.pages.storage_UI import Ui_Form


class Storage(QWidget):
    def __init__(self):
        super(Storage, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)