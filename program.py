# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(854, 708)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 140, 101, 31))
        self.label.setObjectName("label")
        self.picsave = QtWidgets.QLineEdit(Form)
        self.picsave.setGeometry(QtCore.QRect(130, 150, 251, 20))
        self.picsave.setObjectName("picsave")
        self.ConfirmButton1 = QtWidgets.QPushButton(Form)
        self.ConfirmButton1.setGeometry(QtCore.QRect(390, 150, 75, 23))
        self.ConfirmButton1.setObjectName("ConfirmButton1")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(390, 230, 81, 31))
        self.addButton.setObjectName("addButton")
        self.TrainButton = QtWidgets.QPushButton(Form)
        self.TrainButton.setGeometry(QtCore.QRect(120, 250, 81, 41))
        self.TrainButton.setObjectName("TrainButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 111, 21))
        self.label_3.setObjectName("label_3")
        self.picname = QtWidgets.QLineEdit(Form)
        self.picname.setGeometry(QtCore.QRect(130, 200, 61, 20))
        self.picname.setObjectName("picname")
        self.BeginButton = QtWidgets.QPushButton(Form)
        self.BeginButton.setGeometry(QtCore.QRect(180, 340, 101, 41))
        self.BeginButton.setObjectName("BeginButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 200, 111, 21))
        self.label_4.setObjectName("label_4")
        self.picnumber = QtWidgets.QLineEdit(Form)
        self.picnumber.setGeometry(QtCore.QRect(260, 200, 61, 20))
        self.picnumber.setObjectName("picnumber")
        self.RecordButton = QtWidgets.QPushButton(Form)
        self.RecordButton.setGeometry(QtCore.QRect(390, 190, 81, 31))
        self.RecordButton.setObjectName("RecordButton")
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(390, 270, 81, 31))
        self.searchButton.setObjectName("searchButton")
        self.changeButton = QtWidgets.QPushButton(Form)
        self.changeButton.setGeometry(QtCore.QRect(390, 310, 81, 31))
        self.changeButton.setObjectName("changeButton")
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setGeometry(QtCore.QRect(390, 350, 81, 31))
        self.deleteButton.setObjectName("deleteButton")
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setGeometry(QtCore.QRect(40, 340, 101, 41))
        self.refreshButton.setObjectName("refreshButton")
        self.checkButton = QtWidgets.QPushButton(Form)
        self.checkButton.setGeometry(QtCore.QRect(260, 250, 81, 41))
        self.checkButton.setObjectName("checkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "人物图片保存地址："))
        self.ConfirmButton1.setText(_translate("Form", "确认"))
        self.addButton.setText(_translate("Form", "员工数据增加"))
        self.TrainButton.setText(_translate("Form", "员工信息处理"))
        self.label_3.setText(_translate("Form", "人物姓名 ："))
        self.BeginButton.setText(_translate("Form", "打卡"))
        self.label_4.setText(_translate("Form", "工号："))
        self.RecordButton.setText(_translate("Form", "录入照片"))
        self.searchButton.setText(_translate("Form", "员工数据查询"))
        self.changeButton.setText(_translate("Form", "员工数据更改"))
        self.deleteButton.setText(_translate("Form", "员工数据删除"))
        self.refreshButton.setText(_translate("Form", "刷新"))
        self.checkButton.setText(_translate("Form", "迟到员工查询"))
