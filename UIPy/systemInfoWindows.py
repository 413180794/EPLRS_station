# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'systemInfoWindows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(661, 391)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 661, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self._system_info_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self._system_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self._system_info_label.setObjectName("_system_info_label")
        self.horizontalLayout_7.addWidget(self._system_info_label)
        self.system_info_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.system_info_label.setText("")
        self.system_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.system_info_label.setObjectName("system_info_label")
        self.horizontalLayout_7.addWidget(self.system_info_label)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cpu_tempe_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cpu_tempe_label.setText("")
        self.cpu_tempe_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_tempe_label.setObjectName("cpu_tempe_label")
        self.horizontalLayout.addWidget(self.cpu_tempe_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cpu_used_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cpu_used_label.setText("")
        self.cpu_used_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_used_label.setObjectName("cpu_used_label")
        self.horizontalLayout_2.addWidget(self.cpu_used_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.ram_total_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ram_total_label.setText("")
        self.ram_total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_total_label.setObjectName("ram_total_label")
        self.horizontalLayout_3.addWidget(self.ram_total_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.ram_used_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ram_used_label.setText("")
        self.ram_used_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_used_label.setObjectName("ram_used_label")
        self.horizontalLayout_4.addWidget(self.ram_used_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.disk_total_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.disk_total_label.setText("")
        self.disk_total_label.setAlignment(QtCore.Qt.AlignCenter)
        self.disk_total_label.setObjectName("disk_total_label")
        self.horizontalLayout_5.addWidget(self.disk_total_label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.disk_used_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.disk_used_label.setText("")
        self.disk_used_label.setAlignment(QtCore.Qt.AlignCenter)
        self.disk_used_label.setObjectName("disk_used_label")
        self.horizontalLayout_6.addWidget(self.disk_used_label)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.voice_card_status_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.voice_card_status_label.setText("")
        self.voice_card_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.voice_card_status_label.setObjectName("voice_card_status_label")
        self.horizontalLayout_8.addWidget(self.voice_card_status_label)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.net_card_status_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.net_card_status_label.setText("")
        self.net_card_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.net_card_status_label.setObjectName("net_card_status_label")
        self.horizontalLayout_9.addWidget(self.net_card_status_label)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setGeometry(QtCore.QRect(550, 340, 101, 41))
        self.close_button.setObjectName("close_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "系统自检"))
        self._system_info_label.setText(_translate("Dialog", "系统信息"))
        self.label_2.setText(_translate("Dialog", "CPU温度"))
        self.label_3.setText(_translate("Dialog", "CPU使用率"))
        self.label_5.setText(_translate("Dialog", "内存容量"))
        self.label_7.setText(_translate("Dialog", "内存用量"))
        self.label_9.setText(_translate("Dialog", "硬盘容量"))
        self.label_11.setText(_translate("Dialog", "硬盘使用率"))
        self.label_15.setText(_translate("Dialog", "声卡状态"))
        self.label_17.setText(_translate("Dialog", "网卡状态"))
        self.close_button.setText(_translate("Dialog", "关闭"))

