# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 781, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.MainWindow_tab = QtWidgets.QWidget()
        self.MainWindow_tab.setObjectName("MainWindow_tab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.MainWindow_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(500, 0, 261, 151))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.__send_rate_main_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__send_rate_main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__send_rate_main_label.setObjectName("__send_rate_main_label")
        self.horizontalLayout_11.addWidget(self.__send_rate_main_label)
        self.send_rate_LCD = QtWidgets.QLCDNumber(self.verticalLayoutWidget_4)
        self.send_rate_LCD.setObjectName("send_rate_LCD")
        self.horizontalLayout_11.addWidget(self.send_rate_LCD)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.__if_connected_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__if_connected_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__if_connected_label.setObjectName("__if_connected_label")
        self.horizontalLayout_13.addWidget(self.__if_connected_label)
        self.if_connected_main = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.if_connected_main.setAlignment(QtCore.Qt.AlignCenter)
        self.if_connected_main.setObjectName("if_connected_main")
        self.horizontalLayout_13.addWidget(self.if_connected_main)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.__other_equip_ID_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__other_equip_ID_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__other_equip_ID_label.setObjectName("__other_equip_ID_label")
        self.horizontalLayout_19.addWidget(self.__other_equip_ID_label)
        self.other_equip_id = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.other_equip_id.setText("")
        self.other_equip_id.setAlignment(QtCore.Qt.AlignCenter)
        self.other_equip_id.setObjectName("other_equip_id")
        self.horizontalLayout_19.addWidget(self.other_equip_id)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.__other_equip_IP_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__other_equip_IP_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__other_equip_IP_label.setObjectName("__other_equip_IP_label")
        self.horizontalLayout_3.addWidget(self.__other_equip_IP_label)
        self.other_equip_ip = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.other_equip_ip.setText("")
        self.other_equip_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.other_equip_ip.setObjectName("other_equip_ip")
        self.horizontalLayout_3.addWidget(self.other_equip_ip)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.__not_read_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__not_read_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__not_read_label.setObjectName("__not_read_label")
        self.horizontalLayout_2.addWidget(self.__not_read_label)
        self.not_read_count_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.not_read_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.not_read_count_label.setObjectName("not_read_count_label")
        self.horizontalLayout_2.addWidget(self.not_read_count_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MainWindow_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 250, 771, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.send_position_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.send_position_button.setObjectName("send_position_button")
        self.horizontalLayout.addWidget(self.send_position_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.send_measure_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.send_measure_button.setObjectName("send_measure_button")
        self.horizontalLayout.addWidget(self.send_measure_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.set_property_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.set_property_button.setObjectName("set_property_button")
        self.horizontalLayout.addWidget(self.set_property_button)
        self.ip_id_table = QtWidgets.QTableWidget(self.MainWindow_tab)
        self.ip_id_table.setGeometry(QtCore.QRect(0, 0, 501, 251))
        self.ip_id_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ip_id_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.ip_id_table.setColumnCount(2)
        self.ip_id_table.setObjectName("ip_id_table")
        self.ip_id_table.setRowCount(0)
        self.ip_id_table.horizontalHeader().setCascadingSectionResizes(False)
        self.ip_id_table.horizontalHeader().setSortIndicatorShown(False)
        self.ip_id_table.horizontalHeader().setStretchLastSection(False)
        self.ip_id_table.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.MainWindow_tab, "")
        self.Position_tab = QtWidgets.QWidget()
        self.Position_tab.setObjectName("Position_tab")
        self.position_table = QtWidgets.QTableWidget(self.Position_tab)
        self.position_table.setGeometry(QtCore.QRect(0, 0, 771, 351))
        self.position_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.position_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.position_table.setColumnCount(4)
        self.position_table.setObjectName("position_table")
        self.position_table.setRowCount(0)
        self.position_table.horizontalHeader().setCascadingSectionResizes(False)
        self.position_table.horizontalHeader().setSortIndicatorShown(False)
        self.position_table.horizontalHeader().setStretchLastSection(False)
        self.position_table.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.Position_tab, "")
        self.Measure_tab = QtWidgets.QWidget()
        self.Measure_tab.setObjectName("Measure_tab")
        self.measure_table = QtWidgets.QTableWidget(self.Measure_tab)
        self.measure_table.setGeometry(QtCore.QRect(0, 0, 771, 361))
        self.measure_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.measure_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.measure_table.setColumnCount(3)
        self.measure_table.setObjectName("measure_table")
        self.measure_table.setRowCount(0)
        self.measure_table.horizontalHeader().setCascadingSectionResizes(False)
        self.measure_table.horizontalHeader().setSortIndicatorShown(False)
        self.measure_table.horizontalHeader().setStretchLastSection(False)
        self.measure_table.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.Measure_tab, "")
        self.Property_tab = QtWidgets.QWidget()
        self.Property_tab.setObjectName("Property_tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Property_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.__send_rate_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.__send_rate_label.setAutoFillBackground(False)
        self.__send_rate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__send_rate_label.setObjectName("__send_rate_label")
        self.horizontalLayout_5.addWidget(self.__send_rate_label)
        self.send_rate_spinbox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.send_rate_spinbox.setMaximum(375.0)
        self.send_rate_spinbox.setSingleStep(0.01)
        self.send_rate_spinbox.setObjectName("send_rate_spinbox")
        self.horizontalLayout_5.addWidget(self.send_rate_spinbox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.__interface_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.__interface_label.setAutoFillBackground(False)
        self.__interface_label.setObjectName("__interface_label")
        self.horizontalLayout_9.addWidget(self.__interface_label, 0, QtCore.Qt.AlignHCenter)
        self.interface_combox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.interface_combox.setObjectName("interface_combox")
        self.interface_combox.addItem("")
        self.interface_combox.addItem("")
        self.horizontalLayout_9.addWidget(self.interface_combox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.__position_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.__position_label.setAutoFillBackground(False)
        self.__position_label.setObjectName("__position_label")
        self.horizontalLayout_12.addWidget(self.__position_label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.position_x_lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.position_x_lcdNumber.setDigitCount(7)
        self.position_x_lcdNumber.setObjectName("position_x_lcdNumber")
        self.horizontalLayout_7.addWidget(self.position_x_lcdNumber)
        self.position_y_lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.position_y_lcdNumber.setDigitCount(7)
        self.position_y_lcdNumber.setObjectName("position_y_lcdNumber")
        self.horizontalLayout_7.addWidget(self.position_y_lcdNumber)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.__temperature_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.__temperature_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.__temperature_label.setAutoFillBackground(False)
        self.__temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__temperature_label.setObjectName("__temperature_label")
        self.horizontalLayout_14.addWidget(self.__temperature_label)
        self.temperature_lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.temperature_lcdNumber.setDigitCount(10)
        self.temperature_lcdNumber.setObjectName("temperature_lcdNumber")
        self.horizontalLayout_14.addWidget(self.temperature_lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.__width_band_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.__width_band_label.setAutoFillBackground(False)
        self.__width_band_label.setObjectName("__width_band_label")
        self.horizontalLayout_4.addWidget(self.__width_band_label, 0, QtCore.Qt.AlignHCenter)
        self.width_band_combox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.width_band_combox.setObjectName("width_band_combox")
        self.width_band_combox.addItem("")
        self.width_band_combox.addItem("")
        self.width_band_combox.addItem("")
        self.width_band_combox.addItem("")
        self.horizontalLayout_4.addWidget(self.width_band_combox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.__interval_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.__interval_label.setAutoFillBackground(False)
        self.__interval_label.setObjectName("__interval_label")
        self.horizontalLayout_6.addWidget(self.__interval_label, 0, QtCore.Qt.AlignHCenter)
        self.interval_combox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.interval_combox.setObjectName("interval_combox")
        self.interval_combox.addItem("")
        self.interval_combox.addItem("")
        self.horizontalLayout_6.addWidget(self.interval_combox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.__routing_parameters_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.__routing_parameters_label.setAutoFillBackground(False)
        self.__routing_parameters_label.setObjectName("__routing_parameters_label")
        self.horizontalLayout_8.addWidget(self.__routing_parameters_label, 0, QtCore.Qt.AlignHCenter)
        self.routing_parameters_combox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.routing_parameters_combox.setObjectName("routing_parameters_combox")
        self.routing_parameters_combox.addItem("")
        self.routing_parameters_combox.addItem("")
        self.horizontalLayout_8.addWidget(self.routing_parameters_combox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.line = QtWidgets.QFrame(self.Property_tab)
        self.line.setGeometry(QtCore.QRect(579, 90, 21, 171))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Property_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(599, 13, 161, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.send_rate_dial = QtWidgets.QDial(self.verticalLayoutWidget_2)
        self.send_rate_dial.setMaximum(375)
        self.send_rate_dial.setSingleStep(0)
        self.send_rate_dial.setProperty("value", 17)
        self.send_rate_dial.setNotchesVisible(False)
        self.send_rate_dial.setObjectName("send_rate_dial")
        self.verticalLayout_2.addWidget(self.send_rate_dial)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.property_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.property_save_button.setObjectName("property_save_button")
        self.verticalLayout_2.addWidget(self.property_save_button)
        self.tabWidget.addTab(self.Property_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.set_property = QtWidgets.QAction(MainWindow)
        self.set_property.setObjectName("set_property")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.__send_rate_main_label.setText(_translate("MainWindow", "发送速率"))
        self.__if_connected_label.setText(_translate("MainWindow", "连通状态"))
        self.if_connected_main.setText(_translate("MainWindow", "未连接"))
        self.__other_equip_ID_label.setText(_translate("MainWindow", "对方设备ID"))
        self.__other_equip_IP_label.setText(_translate("MainWindow", "对方设备IP"))
        self.__not_read_label.setText(_translate("MainWindow", "未读消息个数"))
        self.not_read_count_label.setText(_translate("MainWindow", "0"))
        self.send_position_button.setText(_translate("MainWindow", "位置报告"))
        self.send_measure_button.setText(_translate("MainWindow", "测量报告"))
        self.set_property_button.setText(_translate("MainWindow", "配置属性"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainWindow_tab), _translate("MainWindow", "主界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Position_tab), _translate("MainWindow", "位置数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Measure_tab), _translate("MainWindow", "测量数据"))
        self.__send_rate_label.setText(_translate("MainWindow", "发送速率"))
        self.send_rate_spinbox.setSuffix(_translate("MainWindow", "Kb/s"))
        self.__interface_label.setText(_translate("MainWindow", "网口串口"))
        self.interface_combox.setItemText(0, _translate("MainWindow", "网口"))
        self.interface_combox.setItemText(1, _translate("MainWindow", "串口"))
        self.__position_label.setText(_translate("MainWindow", "经纬度"))
        self.__temperature_label.setText(_translate("MainWindow", "温度"))
        self.__width_band_label.setText(_translate("MainWindow", "频率间隔"))
        self.width_band_combox.setItemText(0, _translate("MainWindow", "30MHz~90MHz"))
        self.width_band_combox.setItemText(1, _translate("MainWindow", "610MHz~690MHz"))
        self.width_band_combox.setItemText(2, _translate("MainWindow", "225MHz~512MHz"))
        self.width_band_combox.setItemText(3, _translate("MainWindow", "1350MHz~1850MHz"))
        self.__interval_label.setText(_translate("MainWindow", "信道间隔"))
        self.interval_combox.setItemText(0, _translate("MainWindow", "25kHz"))
        self.interval_combox.setItemText(1, _translate("MainWindow", "625kHz"))
        self.__routing_parameters_label.setText(_translate("MainWindow", "路由协议"))
        self.routing_parameters_combox.setItemText(0, _translate("MainWindow", "OSPF协议"))
        self.routing_parameters_combox.setItemText(1, _translate("MainWindow", "testError"))
        self.property_save_button.setText(_translate("MainWindow", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Property_tab), _translate("MainWindow", "属性"))
        self.set_property.setText(_translate("MainWindow", "属性..."))

import DTresource_rc
