# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_collecting.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckInUi(object):
    def setupUi(self, CheckInUi):
        CheckInUi.setObjectName("CheckInUi")
        CheckInUi.resize(692, 539)
        CheckInUi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(128,128,128);\n"
"")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(CheckInUi)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.checkin_box = QtWidgets.QVBoxLayout()
        self.checkin_box.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.checkin_box.setSpacing(0)
        self.checkin_box.setObjectName("checkin_box")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.checkin_box.addItem(spacerItem1)
        self.label_camera_layout = QtWidgets.QLabel(CheckInUi)
        self.label_camera_layout.setStyleSheet("background-image: url(:/icons/camera_bkg.png);")
        self.label_camera_layout.setText("")
        self.label_camera_layout.setObjectName("label_camera_layout")
        self.checkin_box.addWidget(self.label_camera_layout)
        self.bt_checkin_box = QtWidgets.QGroupBox(CheckInUi)
        self.bt_checkin_box.setStyleSheet("border-style:none;")
        self.bt_checkin_box.setTitle("")
        self.bt_checkin_box.setFlat(True)
        self.bt_checkin_box.setCheckable(False)
        self.bt_checkin_box.setObjectName("bt_checkin_box")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.bt_checkin_box)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(211, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.bt_face_collecting = QtWidgets.QPushButton(self.bt_checkin_box)
        font = QtGui.QFont()
        font.setFamily("MF LiHei (Noncommercial)")
        font.setPointSize(25)
        self.bt_face_collecting.setFont(font)
        self.bt_face_collecting.setStyleSheet("border-style:solid ;\n"
"border-width:1px;\n"
"background-color:rgb(255,183,134);\n"
"color:white;\n"
"border:10px;\n"
"border-radius:10px;\n"
"padding:7px 10px;")
        self.bt_face_collecting.setDefault(False)
        self.bt_face_collecting.setFlat(False)
        self.bt_face_collecting.setObjectName("bt_face_collecting")
        self.horizontalLayout_4.addWidget(self.bt_face_collecting)
        spacerItem3 = QtWidgets.QSpacerItem(211, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 2)
        self.checkin_box.addWidget(self.bt_checkin_box)
        self.groupBox = QtWidgets.QGroupBox(CheckInUi)
        self.groupBox.setStyleSheet("border-style:none")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setStyleSheet("color:rgb(0, 0, 0)")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_collected_num = QtWidgets.QLabel(self.groupBox_2)
        self.label_collected_num.setStyleSheet("background-color: rgb(255,246,234);\n"
"color:rgb(0, 0, 0)")
        self.label_collected_num.setText("")
        self.label_collected_num.setObjectName("label_collected_num")
        self.horizontalLayout.addWidget(self.label_collected_num)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_collect_sum = QtWidgets.QLabel(self.groupBox_2)
        self.label_collect_sum.setStyleSheet("background-color: rgb(255,246,234);\n"
"color:rgb(0, 0, 0)\n"
"")
        self.label_collect_sum.setText("")
        self.label_collect_sum.setObjectName("label_collect_sum")
        self.horizontalLayout.addWidget(self.label_collect_sum)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 2)
        self.checkin_box.addWidget(self.groupBox)
        self.label_checkin_note_box = QtWidgets.QGroupBox(CheckInUi)
        self.label_checkin_note_box.setStyleSheet("border-style:none;")
        self.label_checkin_note_box.setTitle("")
        self.label_checkin_note_box.setFlat(True)
        self.label_checkin_note_box.setObjectName("label_checkin_note_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.label_checkin_note_box)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(141, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_collecting_note = QtWidgets.QLabel(self.label_checkin_note_box)
        self.label_collecting_note.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_collecting_note.setText("")
        self.label_collecting_note.setAlignment(QtCore.Qt.AlignCenter)
        self.label_collecting_note.setObjectName("label_collecting_note")
        self.horizontalLayout_3.addWidget(self.label_collecting_note)
        spacerItem7 = QtWidgets.QSpacerItem(141, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.checkin_box.addWidget(self.label_checkin_note_box)
        self.checkin_box.setStretch(0, 1)
        self.checkin_box.setStretch(1, 15)
        self.checkin_box.setStretch(2, 1)
        self.checkin_box.setStretch(3, 1)
        self.checkin_box.setStretch(4, 2)
        self.horizontalLayout_2.addLayout(self.checkin_box)
        self.staff_box = QtWidgets.QGroupBox(CheckInUi)
        self.staff_box.setStyleSheet("border-top-color: rgb(255, 255, 255);")
        self.staff_box.setTitle("")
        self.staff_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.staff_box.setFlat(True)
        self.staff_box.setObjectName("staff_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.staff_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(20, 558, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.bt_staffInformation_box = QtWidgets.QGroupBox(self.staff_box)
        self.bt_staffInformation_box.setStyleSheet("background-color: transparent;\n"
"border-style:none;")
        self.bt_staffInformation_box.setTitle("")
        self.bt_staffInformation_box.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.bt_staffInformation_box.setFlat(True)
        self.bt_staffInformation_box.setCheckable(False)
        self.bt_staffInformation_box.setObjectName("bt_staffInformation_box")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bt_staffInformation_box)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2.addWidget(self.bt_staffInformation_box)
        self.verticalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.addWidget(self.staff_box)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 2)

        self.retranslateUi(CheckInUi)
        QtCore.QMetaObject.connectSlotsByName(CheckInUi)

    def retranslateUi(self, CheckInUi):
        _translate = QtCore.QCoreApplication.translate
        CheckInUi.setWindowTitle(_translate("CheckInUi", "Form"))
        self.bt_face_collecting.setText(_translate("CheckInUi", "开 始 采 集"))
        self.label.setText(_translate("CheckInUi", "已采集"))
        self.label_5.setText(_translate("CheckInUi", "/"))
        self.label_2.setText(_translate("CheckInUi", "张"))
import icons_rc
