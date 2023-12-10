from PyQt5.QtWidgets import QWidget
from ui.pages.sftp_UI import Ui_Form


class SFTP(QWidget):
    def __init__(self):
        super(SFTP, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
