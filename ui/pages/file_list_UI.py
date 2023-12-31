# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\file_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 475)
        Form.setStyleSheet("#Form {\n"
"    background-color: #A0B9D0;\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.files = QtWidgets.QTreeWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.files.sizePolicy().hasHeightForWidth())
        self.files.setSizePolicy(sizePolicy)
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
"    border-top-right:5px;\n"
"    padding-left:10px;\n"
"    padding-bottom:20px        \n"
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
        self.files.setIconSize(QtCore.QSize(16, 16))
        self.files.setObjectName("files")
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        font.setBold(True)
        self.files.headerItem().setFont(0, font)
        self.files.headerItem().setBackground(0, QtGui.QColor(255, 255, 255))
        item_0 = QtWidgets.QTreeWidgetItem(self.files)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item_0.setFont(0, font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/icons/feather/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.files)
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.files)
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout.addWidget(self.files, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.files.headerItem().setText(0, _translate("Form", "File list"))
        __sortingEnabled = self.files.isSortingEnabled()
        self.files.setSortingEnabled(False)
        self.files.topLevelItem(0).setText(0, _translate("Form", "Fade"))
        self.files.topLevelItem(0).child(0).setText(0, _translate("Form", "Sova"))
        self.files.topLevelItem(0).child(0).child(0).setText(0, _translate("Form", "Sage"))
        self.files.topLevelItem(1).setText(0, _translate("Form", "Omen"))
        self.files.topLevelItem(1).child(0).setText(0, _translate("Form", "Cypher"))
        self.files.topLevelItem(2).setText(0, _translate("Form", "Breach"))
        self.files.topLevelItem(2).child(0).setText(0, _translate("Form", "Yoru"))
        self.files.setSortingEnabled(__sortingEnabled)
from static import res_rc
