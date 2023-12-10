import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QPoint, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap

from ui.MainWindow_3_UI import Ui_MainWindow

from pages_functions.cpu_and_memory import CPU_and_Memory
from pages_functions.sys_info import System_Information
from pages_functions.os_info import OS_Info
from pages_functions.process_list import Process_List
from pages_functions.file_list import File_List
from pages_functions.terminal import Terminal
from pages_functions.sftp import SFTP
from pages_functions.storage import Storage
from pages_functions.network import Network

class MyWindow_3(QMainWindow):
    logoutSignal_3 = pyqtSignal()
    def __init__(self):
        super(MyWindow_3, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._starPos = None
        self._endPos = None
        self._tracking = False

        # Get all objects in window
        self.cpu_button = self.ui.cpu_button
        self.sy_info_button = self.ui.sy_info_button
        self.os_info_button = self.ui.os_info_button
        self.process_list_button = self.ui.process_list_button
        self.file_list_button = self.ui.file_list_button
        self.terminal_button = self.ui.terminal_button
        self.sftp_button = self.ui.sftp_button
        self.storage_button = self.ui.storage_button
        self.network_button = self.ui.network_button
        
        ##Create dict for menu buttons and tab windows
        self.menu_btn_dict = {
            self.cpu_button: CPU_and_Memory,
            self.sy_info_button: System_Information,
            self.os_info_button: OS_Info,
            self.process_list_button: Process_List,
            self.file_list_button: File_List,
            self.terminal_button: Terminal,
            self.sftp_button: SFTP,
            self.storage_button: Storage,
            self.network_button: Network,
        }

        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        # show home window when start app

        self.show_home_window_3()
        #connect signal and slot
        self.cpu_button.clicked.connect(self.show_selected_window)
        self.sy_info_button.clicked.connect(self.show_selected_window)
        self.os_info_button.clicked.connect(self.show_selected_window)
        self.process_list_button.clicked.connect(self.show_selected_window)
        self.file_list_button.clicked.connect(self.show_selected_window)
        self.terminal_button.clicked.connect(self.show_selected_window)
        self.sftp_button.clicked.connect(self.show_selected_window)
        self.storage_button.clicked.connect(self.show_selected_window)
        self.network_button.clicked.connect(self.show_selected_window)

        #hide the frame and background of the app
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def show_home_window_3(self):
        result = self.open_tab_flag(self.cpu_button)
        self.set_btn_checked(self.cpu_button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = self.cpu_button.text()
            curIndex = self.ui.tabWidget.addTab(CPU_and_Memory(), tab_title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def set_btn_checked(self, btn):
        for button in self.menu_btn_dict.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)

    def show_selected_window(self):
        # show selected window
        button = self.sender()
        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)
        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btn_dict[button](), tab_title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def open_tab_flag(self, btn_text):
        # check selected window show or not
        open_tab_count = self.ui.tabWidget.count()
        for i in range(open_tab_count):
            tab_title = self.ui.tabWidget.tabText(i)
            if tab_title == btn_text:
                return True, i
            else:
                continue
        return False,

    def close_tab(self, index):
        self.ui.tabWidget.removeTab(index)
        if self.ui.tabWidget.count() == 0:
            self.ui.toolBox.setCurrentIndex(0)
            self.show_home_window_3()


    ## TODO: make the window movable after hide window frame
    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self._tracking:
            self._endPos = a0.pos() - self._starPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._starPos = QPoint(a0.x(), a0.y())
            self._tracking = True

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._tracking = False
            self._starPos = None
            self._endPos = None 