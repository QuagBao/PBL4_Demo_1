# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\storage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 338)
        Form.setStyleSheet("background-color: #A0B9D0;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_93 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        self.label_93.setFont(font)
        self.label_93.setObjectName("label_93")
        self.verticalLayout.addWidget(self.label_93)
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_93.setText(_translate("Form", "Disk Partition"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Device"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Total Storage"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Used Storage"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Free Storage"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Percent"))
from static import res_rc