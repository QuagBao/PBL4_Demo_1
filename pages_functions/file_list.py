from PyQt5.QtWidgets import QWidget
from ui.pages.file_list_UI import Ui_Form


class File_List(QWidget):
    def __init__(self):
        super(File_List, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
