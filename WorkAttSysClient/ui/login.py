# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 342)
        Form.setStyleSheet("QWidget{Background-color:rgb(255,246,234);\n"
"color:rgb(0,0,0);}\n"
"")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QPushButton{border-style:solid ;\n"
"border-width:1px;\n"
"background-color:rgb(255,183,134);\n"
"color:white;\n"
"border:10px;\n"
"border-radius:10px;\n"
"padding:6px 10px;}\n"
"QLineEdit{border: 1px solid rgb(249,179,132,30%);border-radius: 3px;background-color:rgb(249,179,132,30%)}\n"
"QLineEdit::hover{border: 1px solid #C0C4CC;}")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.user_Label = QtWidgets.QLabel(self.frame)
        self.user_Label.setStyleSheet("color:rgb(0, 0, 0)")
        self.user_Label.setObjectName("user_Label")
        self.horizontalLayout_2.addWidget(self.user_Label)
        self.user_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.user_lineEdit.setStyleSheet("\n"
"")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.horizontalLayout_2.addWidget(self.user_lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayout_2.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pwd_Label = QtWidgets.QLabel(self.frame)
        self.pwd_Label.setStyleSheet("color:rgb(0, 0, 0)")
        self.pwd_Label.setObjectName("pwd_Label")
        self.horizontalLayout_3.addWidget(self.pwd_Label)
        self.pwd_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.pwd_lineEdit.setStyleSheet("")
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.horizontalLayout_3.addWidget(self.pwd_lineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.chk_psw = QtWidgets.QCheckBox(self.frame)
        self.chk_psw.setObjectName("chk_psw")
        self.horizontalLayout_6.addWidget(self.chk_psw)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.cancel_Button = QtWidgets.QPushButton(self.frame)
        self.cancel_Button.setStyleSheet("")
        self.cancel_Button.setObjectName("cancel_Button")
        self.horizontalLayout.addWidget(self.cancel_Button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.login_Button = QtWidgets.QPushButton(self.frame)
        self.login_Button.setStyleSheet("")
        self.login_Button.setObjectName("login_Button")
        self.horizontalLayout.addWidget(self.login_Button)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.register_Button = QtWidgets.QPushButton(self.frame)
        self.register_Button.setStyleSheet("")
        self.register_Button.setObjectName("register_Button")
        self.horizontalLayout.addWidget(self.register_Button)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_login_msg = QtWidgets.QLabel(self.frame)
        self.label_login_msg.setText("")
        self.label_login_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login_msg.setObjectName("label_login_msg")
        self.verticalLayout.addWidget(self.label_login_msg)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 2)
        self.verticalLayout.setStretch(7, 1)
        self.horizontalLayout_4.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.user_Label.setText(_translate("Form", "工号："))
        self.pwd_Label.setText(_translate("Form", "密码："))
        self.chk_psw.setText(_translate("Form", "记住密码"))
        self.cancel_Button.setText(_translate("Form", "退 出"))
        self.login_Button.setText(_translate("Form", "登 录"))
        self.register_Button.setText(_translate("Form", "注 册"))
