from PyQt5.QtWidgets import QWidget
from ui.pages.network_UI import Ui_Form


class Network(QWidget):
    def __init__(self):
        super(Network, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)