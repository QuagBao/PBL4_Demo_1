# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 669)
        MainWindow.setStyleSheet("background-color: #C9D8E3;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #C9D8E3;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setStyleSheet("background-color: #C9D8E3;")
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.menu_widget = QtWidgets.QWidget(self.splitter)
        self.menu_widget.setStyleSheet("background-color: #4B7C9B;\n"
"color: #0E243D;\n"
"\n"
"")
        self.menu_widget.setObjectName("menu_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_widget)
        self.gridLayout.setContentsMargins(5, 5, 5, 20)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.menu_widget)
        self.toolBox.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("#toolBox{\n"
"    color:#8DAEC6;\n"
"    border-radius: 5%;\n"
"}\n"
"#toolBox::tab{\n"
"    padding-left:5px;\n"
"    text-align:left;\n"
"    border-radius:5px;\n"
"}\n"
"#toolBox::tab::hover{\n"
"    background-color:#82A7C2;\n"
"}\n"
"#toolBox::tab::selected{\n"
"    background-color:#8DAEC6;\n"
"    font-weight:bold;\n"
"}\n"
"#toolBox QPushButton{\n"
"    padding: 5px 0px 5px 20px;\n"
"    text-align:left;\n"
"    border-radius:5px;\n"
"    color: #11253E;\n"
"    border: 1px;\n"
"}\n"
"#toolBox QPushButton:hover{\n"
"    background-color:#6991B5;\n"
"}\n"
"#toolBox QPushButton:checked{\n"
"    background-color:#78A0BC;\n"
"}\n"
"")
        self.toolBox.setObjectName("toolBox")
        self.general_page = QtWidgets.QWidget()
        self.general_page.setGeometry(QtCore.QRect(0, 0, 161, 551))
        self.general_page.setObjectName("general_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.general_page)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_button = QtWidgets.QPushButton(self.general_page)
        self.home_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.home_button.setCheckable(True)
        self.home_button.setChecked(False)
        self.home_button.setObjectName("home_button")
        self.verticalLayout.addWidget(self.home_button)
        self.dashboard_button = QtWidgets.QPushButton(self.general_page)
        self.dashboard_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dashboard_button.setCheckable(True)
        self.dashboard_button.setObjectName("dashboard_button")
        self.verticalLayout.addWidget(self.dashboard_button)
        spacerItem = QtWidgets.QSpacerItem(20, 414, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Img/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.general_page, icon, "")
        self.car_page = QtWidgets.QWidget()
        self.car_page.setGeometry(QtCore.QRect(0, 0, 161, 551))
        self.car_page.setObjectName("car_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.car_page)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toyota_button = QtWidgets.QPushButton(self.car_page)
        self.toyota_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toyota_button.setStyleSheet("")
        self.toyota_button.setCheckable(True)
        self.toyota_button.setObjectName("toyota_button")
        self.verticalLayout_2.addWidget(self.toyota_button)
        self.lexus_button = QtWidgets.QPushButton(self.car_page)
        self.lexus_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lexus_button.setCheckable(True)
        self.lexus_button.setObjectName("lexus_button")
        self.verticalLayout_2.addWidget(self.lexus_button)
        self.mazda_button = QtWidgets.QPushButton(self.car_page)
        self.mazda_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mazda_button.setCheckable(True)
        self.mazda_button.setObjectName("mazda_button")
        self.verticalLayout_2.addWidget(self.mazda_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 378, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Img/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.car_page, icon1, "")
        self.social_page = QtWidgets.QWidget()
        self.social_page.setGeometry(QtCore.QRect(0, 0, 83, 82))
        self.social_page.setObjectName("social_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.social_page)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.youtube_button = QtWidgets.QPushButton(self.social_page)
        self.youtube_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.youtube_button.setCheckable(True)
        self.youtube_button.setObjectName("youtube_button")
        self.verticalLayout_3.addWidget(self.youtube_button)
        self.tumblr_button = QtWidgets.QPushButton(self.social_page)
        self.tumblr_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tumblr_button.setCheckable(True)
        self.tumblr_button.setObjectName("tumblr_button")
        self.verticalLayout_3.addWidget(self.tumblr_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 414, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Img/icons/user-add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.social_page, icon2, "")
        self.gridLayout.addWidget(self.toolBox, 0, 1, 1, 1)
        self.main_widget = QtWidgets.QWidget(self.splitter)
        self.main_widget.setStyleSheet("background-color: #A0B9D0;")
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.search_widget = QtWidgets.QWidget(self.main_widget)
        self.search_widget.setStyleSheet("#search_widget{\n"
"    background-color:#4B7C9B;\n"
"}\n"
"#search_widget QPushButton{\n"
"    border-radius: 5px;\n"
"    padding: 5px 20px 5px 20px;\n"
"    text-align:center;\n"
"}\n"
"#search_widge QPushButton:pressed{\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/*Set style for long and creat device button in function widget */\n"
"#ExitButton:hover, #ExitButton:pressed, #hidden_button:hover, #hidden_button:pressed{\n"
"    background-color: #8DAEC6;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"#AddressConnect{\n"
"    color: #1A3551;\n"
"    border-radius: 8px;\n"
"    padding-left: 10px;\n"
"}\n"
"")
        self.search_widget.setObjectName("search_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_widget)
        self.horizontalLayout.setContentsMargins(9, -1, 9, 9)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hidden_button = QtWidgets.QPushButton(self.search_widget)
        self.hidden_button.setMinimumSize(QtCore.QSize(30, 30))
        self.hidden_button.setMaximumSize(QtCore.QSize(30, 30))
        self.hidden_button.setStyleSheet("#QPushButton{\n"
"    background-color: #4B7C9B;\n"
"    border-radius: 10%\n"
"}\n"
"\n"
"")
        self.hidden_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Img/icons/list.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/Img/icons/menu-burger.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.hidden_button.setIcon(icon3)
        self.hidden_button.setCheckable(True)
        self.hidden_button.setObjectName("hidden_button")
        self.horizontalLayout.addWidget(self.hidden_button)
        spacerItem3 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.AddressConnect = QtWidgets.QLineEdit(self.search_widget)
        self.AddressConnect.setEnabled(False)
        self.AddressConnect.setMinimumSize(QtCore.QSize(331, 22))
        self.AddressConnect.setStyleSheet("background-color: #fff")
        self.AddressConnect.setObjectName("AddressConnect")
        self.horizontalLayout.addWidget(self.AddressConnect)
        spacerItem4 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.ExitButton = QtWidgets.QPushButton(self.search_widget)
        self.ExitButton.setMinimumSize(QtCore.QSize(141, 26))
        self.ExitButton.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Img/icons/log_3596092.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon4)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)
        self.user_label = QtWidgets.QLabel(self.search_widget)
        self.user_label.setMinimumSize(QtCore.QSize(20, 20))
        self.user_label.setMaximumSize(QtCore.QSize(20, 20))
        self.user_label.setStyleSheet("#user_label{\n"
"    background-color:#fff;\n"
"    border:1px solid #F2F4F4;\n"
"    padding:5px 5px;\n"
"    border-radius:10%;\n"
"}\n"
"")
        self.user_label.setText("")
        self.user_label.setPixmap(QtGui.QPixmap(":/Img/icons/settings.svg"))
        self.user_label.setScaledContents(True)
        self.user_label.setObjectName("user_label")
        self.horizontalLayout.addWidget(self.user_label)
        self.gridLayout_2.addWidget(self.search_widget, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("#tabWidget{\n"
"    background-color: #C9D8E3;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::close-button{\n"
"    margin-left:3px;\n"
"    image: url(:/Img/icons/x-mark-4-16.ico);\n"
"}\n"
"QTabBar::close-button:hover{\n"
"    image: url(:/Img/icons/close_10263254.png);\n"
"}\n"
"QTabBar::tab{\n"
"    background-color:  #C9D8E3;\n"
"    min-width: 100px;\n"
"    max-width: 175px;\n"
"    height: 25px;\n"
"    border-radius:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(-1)
        self.hidden_button.toggled['bool'].connect(self.menu_widget.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_button.setText(_translate("MainWindow", "Rasp"))
        self.dashboard_button.setText(_translate("MainWindow", "Dashboard"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.general_page), _translate("MainWindow", "Information"))
        self.toyota_button.setText(_translate("MainWindow", "Toyota"))
        self.lexus_button.setText(_translate("MainWindow", "Lexus"))
        self.mazda_button.setText(_translate("MainWindow", "Mazda"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.car_page), _translate("MainWindow", "Folder"))
        self.youtube_button.setText(_translate("MainWindow", "Youtube"))
        self.tumblr_button.setText(_translate("MainWindow", "Tumbr"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.social_page), _translate("MainWindow", "SendFile"))
        self.AddressConnect.setText(_translate("MainWindow", "IP:                                              Type of connect:"))
        self.ExitButton.setText(_translate("MainWindow", "Disconnect"))
from static import res_rc