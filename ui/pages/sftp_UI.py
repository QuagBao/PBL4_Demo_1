# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sftp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(917, 521)
        Form.setStyleSheet("#Form{\n"
"    background-color: #A0B9D0;\n"
"}\n"
"\n"
"QPushButton{\n"
"    width:100px;\n"
"    height:33px;\n"
"    text-align: center;\n"
"    padding: 3px;\n"
"    font-weight:bold;\n"
"    border-radius:10px;\n"
"    color: #11253E;\n"
"    border: 1px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#6991B5;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    background-color:#78A0BC;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 2)
        self.files = QtWidgets.QTreeWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        self.files.setFont(font)
        self.files.setStyleSheet("QTreeWidget {\n"
"    spacing: 10px; /* Cách nhau 5px giữa các item trong 1 hàng */\n"
"}\n"
"\n"
"#files{\n"
"    background-color: #3E7CB1;\n"
"    border:1px solid #DBE4EE;\n"
"    border-radius: 25px solid #DBE4EE;\n"
"    padding:25px;\n"
"    color: #DBE4EE;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{    color: #DBE4EE;\n"
"    background-color: #3E7CB1;\n"
"    border:1px;\n"
"}\n"
"\n"
"QTreeWidget::item{\n"
"    padding-bottom:5px;        \n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QTreeWidget::item::hover{\n"
"    background-color: #81A4CD;\n"
"    border:1px solid #81A4CD ;\n"
"    border-radius: 5px\n"
"}\n"
"\n"
"QTreeWidget::item::pressed{\n"
"    font-weight: bold;\n"
"    padding-left:5px;\n"
"    background-color: #81A4CD;\n"
"    border:1px solid #81A4CD ;\n"
"    border-radius: 5px\n"
"}\n"
"\n"
"QTreeWidget::item::selected{\n"
"    font-weight: bold;\n"
"    background-color: #81A4CD;\n"
"    border:1px solid #81A4CD ;\n"
"    border-radius: 5px\n"
"}\n"
"\n"
"QTreeWidget::item::selected::active{\n"
"    background-color: #054A91;\n"
"    border:1px solid #81A4CD ;\n"
"    border-radius: 5px;\n"
"    font-weight:bold;\n"
"}")
        self.files.setObjectName("files")
        self.files.headerItem().setText(0, "File List")
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        self.files.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.files)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/icons/feather/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.files)
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.files)
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.gridLayout_2.addWidget(self.files, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.send_file_btn = QtWidgets.QPushButton(self.frame)
        self.send_file_btn.setMinimumSize(QtCore.QSize(145, 39))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.send_file_btn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/icons/feather/share.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_file_btn.setIcon(icon1)
        self.send_file_btn.setIconSize(QtCore.QSize(24, 24))
        self.send_file_btn.setObjectName("send_file_btn")
        self.gridLayout.addWidget(self.send_file_btn, 2, 0, 1, 1)
        self.delete_file_btn = QtWidgets.QPushButton(self.frame)
        self.delete_file_btn.setMinimumSize(QtCore.QSize(144, 39))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.delete_file_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/icons/feather/file-minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_file_btn.setIcon(icon2)
        self.delete_file_btn.setIconSize(QtCore.QSize(24, 24))
        self.delete_file_btn.setObjectName("delete_file_btn")
        self.gridLayout.addWidget(self.delete_file_btn, 1, 1, 1, 1)
        self.new_file_btn = QtWidgets.QPushButton(self.frame)
        self.new_file_btn.setMinimumSize(QtCore.QSize(145, 39))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.new_file_btn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/icons/feather/file-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_file_btn.setIcon(icon3)
        self.new_file_btn.setIconSize(QtCore.QSize(24, 24))
        self.new_file_btn.setObjectName("new_file_btn")
        self.gridLayout.addWidget(self.new_file_btn, 1, 0, 1, 1)
        self.move_down_btn = QtWidgets.QPushButton(self.frame)
        self.move_down_btn.setMinimumSize(QtCore.QSize(144, 39))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.move_down_btn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons/icons/feather/arrow-down-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.move_down_btn.setIcon(icon4)
        self.move_down_btn.setIconSize(QtCore.QSize(24, 24))
        self.move_down_btn.setObjectName("move_down_btn")
        self.gridLayout.addWidget(self.move_down_btn, 0, 1, 1, 1)
        self.move_up_btn = QtWidgets.QPushButton(self.frame)
        self.move_up_btn.setMinimumSize(QtCore.QSize(145, 39))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.move_up_btn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icons/icons/feather/arrow-up-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.move_up_btn.setIcon(icon5)
        self.move_up_btn.setIconSize(QtCore.QSize(24, 24))
        self.move_up_btn.setObjectName("move_up_btn")
        self.gridLayout.addWidget(self.move_up_btn, 0, 0, 1, 1)
        self.receive_file_btn = QtWidgets.QPushButton(self.frame)
        self.receive_file_btn.setMinimumSize(QtCore.QSize(144, 39))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        font.setBold(True)
        self.receive_file_btn.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icons/icons/feather/download.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.receive_file_btn.setIcon(icon6)
        self.receive_file_btn.setIconSize(QtCore.QSize(24, 24))
        self.receive_file_btn.setObjectName("receive_file_btn")
        self.gridLayout.addWidget(self.receive_file_btn, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SFTP"))
        __sortingEnabled = self.files.isSortingEnabled()
        self.files.setSortingEnabled(False)
        self.files.topLevelItem(0).setText(0, _translate("Form", "Khởi tranh"))
        self.files.topLevelItem(0).child(0).setText(0, _translate("Form", "Breach"))
        self.files.topLevelItem(0).child(1).setText(0, _translate("Form", "Sova"))
        self.files.topLevelItem(0).child(2).setText(0, _translate("Form", "Skye"))
        self.files.topLevelItem(1).setText(0, _translate("Form", "Controller"))
        self.files.topLevelItem(1).child(0).setText(0, _translate("Form", "Fade"))
        self.files.topLevelItem(1).child(1).setText(0, _translate("Form", "Reyna"))
        self.files.topLevelItem(2).setText(0, _translate("Form", "Smoke"))
        self.files.topLevelItem(2).child(0).setText(0, _translate("Form", "Omen"))
        self.files.topLevelItem(2).child(0).child(0).setText(0, _translate("Form", "Viper"))
        self.files.setSortingEnabled(__sortingEnabled)
        self.send_file_btn.setText(_translate("Form", "Send File"))
        self.delete_file_btn.setText(_translate("Form", "Delete File"))
        self.new_file_btn.setText(_translate("Form", "New File"))
        self.move_down_btn.setText(_translate("Form", "Move Down"))
        self.move_up_btn.setText(_translate("Form", "Move Up"))
        self.receive_file_btn.setText(_translate("Form", "Receive File"))
from static import res_rc
