# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_back.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 592)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1011, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.MainWindow_tab = QtWidgets.QWidget()
        self.MainWindow_tab.setObjectName("MainWindow_tab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.MainWindow_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(470, 0, 361, 541))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.__position_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__position_label.setAutoFillBackground(False)
        self.__position_label.setObjectName("__position_label")
        self.horizontalLayout_12.addWidget(self.__position_label, 0, QtCore.Qt.AlignHCenter)
        self.position_show = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.position_show.setAutoFillBackground(False)
        self.position_show.setText("")
        self.position_show.setAlignment(QtCore.Qt.AlignCenter)
        self.position_show.setObjectName("position_show")
        self.horizontalLayout_12.addWidget(self.position_show)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self._temperature_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self._temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self._temperature_label.setObjectName("_temperature_label")
        self.horizontalLayout_15.addWidget(self._temperature_label)
        self.temperature_show = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.temperature_show.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_show.setObjectName("temperature_show")
        self.horizontalLayout_15.addWidget(self.temperature_show)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.__if_connected_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__if_connected_label.setAlignment(QtCore.Qt.AlignCenter)
        self.__if_connected_label.setObjectName("__if_connected_label")
        self.horizontalLayout_13.addWidget(self.__if_connected_label)
        self.if_connected_main = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.if_connected_main.setText("")
        self.if_connected_main.setAlignment(QtCore.Qt.AlignCenter)
        self.if_connected_main.setObjectName("if_connected_main")
        self.horizontalLayout_13.addWidget(self.if_connected_main)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.__send_rate_main_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__send_rate_main_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.__send_rate_main_label_2.setObjectName("__send_rate_main_label_2")
        self.horizontalLayout_11.addWidget(self.__send_rate_main_label_2)
        self.send_rate_show = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.send_rate_show.setText("")
        self.send_rate_show.setAlignment(QtCore.Qt.AlignCenter)
        self.send_rate_show.setObjectName("send_rate_show")
        self.horizontalLayout_11.addWidget(self.send_rate_show)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
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
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.__send_states = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.__send_states.setAlignment(QtCore.Qt.AlignCenter)
        self.__send_states.setObjectName("__send_states")
        self.horizontalLayout_7.addWidget(self.__send_states)
        self.send_states_show = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.send_states_show.setAlignment(QtCore.Qt.AlignCenter)
        self.send_states_show.setObjectName("send_states_show")
        self.horizontalLayout_7.addWidget(self.send_states_show)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self._search_device_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self._search_device_label.setFont(font)
        self._search_device_label.setAlignment(QtCore.Qt.AlignCenter)
        self._search_device_label.setObjectName("_search_device_label")
        self.horizontalLayout_14.addWidget(self._search_device_label)
        self.search_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_edit.sizePolicy().hasHeightForWidth())
        self.search_edit.setSizePolicy(sizePolicy)
        self.search_edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.search_edit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.search_edit.setObjectName("search_edit")
        self.horizontalLayout_14.addWidget(self.search_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.ip_id_table = QtWidgets.QTableWidget(self.MainWindow_tab)
        self.ip_id_table.setGeometry(QtCore.QRect(0, 0, 471, 541))
        self.ip_id_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ip_id_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.ip_id_table.setColumnCount(4)
        self.ip_id_table.setObjectName("ip_id_table")
        self.ip_id_table.setRowCount(0)
        self.ip_id_table.horizontalHeader().setCascadingSectionResizes(False)
        self.ip_id_table.horizontalHeader().setSortIndicatorShown(False)
        self.ip_id_table.horizontalHeader().setStretchLastSection(False)
        self.ip_id_table.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(self.MainWindow_tab)
        self.label.setGeometry(QtCore.QRect(840, 0, 161, 161))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.MainWindow_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(830, 160, 171, 381))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.set_property_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_property_button.sizePolicy().hasHeightForWidth())
        self.set_property_button.setSizePolicy(sizePolicy)
        self.set_property_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.set_property_button.setFont(font)
        self.set_property_button.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/setting1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set_property_button.setIcon(icon)
        self.set_property_button.setIconSize(QtCore.QSize(60, 60))
        self.set_property_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.set_property_button.setObjectName("set_property_button")
        self.gridLayout_2.addWidget(self.set_property_button, 3, 0, 1, 1)
        self.send_measure_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_measure_button.sizePolicy().hasHeightForWidth())
        self.send_measure_button.setSizePolicy(sizePolicy)
        self.send_measure_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.send_measure_button.setFont(font)
        self.send_measure_button.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resource/measure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_measure_button.setIcon(icon1)
        self.send_measure_button.setIconSize(QtCore.QSize(60, 60))
        self.send_measure_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.send_measure_button.setObjectName("send_measure_button")
        self.gridLayout_2.addWidget(self.send_measure_button, 0, 1, 1, 1)
        self.start_voice_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_voice_button.sizePolicy().hasHeightForWidth())
        self.start_voice_button.setSizePolicy(sizePolicy)
        self.start_voice_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.start_voice_button.setFont(font)
        self.start_voice_button.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resource/telephone1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_voice_button.setIcon(icon2)
        self.start_voice_button.setIconSize(QtCore.QSize(60, 60))
        self.start_voice_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.start_voice_button.setObjectName("start_voice_button")
        self.gridLayout_2.addWidget(self.start_voice_button, 1, 0, 1, 1)
        self.clear_device_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_device_button.sizePolicy().hasHeightForWidth())
        self.clear_device_button.setSizePolicy(sizePolicy)
        self.clear_device_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.clear_device_button.setFont(font)
        self.clear_device_button.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resource/delete1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_device_button.setIcon(icon3)
        self.clear_device_button.setIconSize(QtCore.QSize(60, 60))
        self.clear_device_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.clear_device_button.setObjectName("clear_device_button")
        self.gridLayout_2.addWidget(self.clear_device_button, 2, 1, 1, 1)
        self.send_position_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_position_button.sizePolicy().hasHeightForWidth())
        self.send_position_button.setSizePolicy(sizePolicy)
        self.send_position_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.send_position_button.setFont(font)
        self.send_position_button.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resource/gps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_position_button.setIcon(icon4)
        self.send_position_button.setIconSize(QtCore.QSize(60, 60))
        self.send_position_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.send_position_button.setObjectName("send_position_button")
        self.gridLayout_2.addWidget(self.send_position_button, 1, 1, 1, 1)
        self.system_check_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_check_button.sizePolicy().hasHeightForWidth())
        self.system_check_button.setSizePolicy(sizePolicy)
        self.system_check_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.system_check_button.setFont(font)
        self.system_check_button.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/resource/checking1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.system_check_button.setIcon(icon5)
        self.system_check_button.setIconSize(QtCore.QSize(60, 60))
        self.system_check_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.system_check_button.setObjectName("system_check_button")
        self.gridLayout_2.addWidget(self.system_check_button, 2, 0, 1, 1)
        self.send_file_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_file_button.sizePolicy().hasHeightForWidth())
        self.send_file_button.setSizePolicy(sizePolicy)
        self.send_file_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.send_file_button.setFont(font)
        self.send_file_button.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/resource/zhihui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_file_button.setIcon(icon6)
        self.send_file_button.setIconSize(QtCore.QSize(60, 60))
        self.send_file_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.send_file_button.setObjectName("send_file_button")
        self.gridLayout_2.addWidget(self.send_file_button, 0, 0, 1, 1)
        self.reset_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/resource/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon7)
        self.reset_button.setIconSize(QtCore.QSize(60, 60))
        self.reset_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.reset_button.setObjectName("reset_button")
        self.gridLayout_2.addWidget(self.reset_button, 3, 1, 1, 1)
        self.update_system_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_system_button.sizePolicy().hasHeightForWidth())
        self.update_system_button.setSizePolicy(sizePolicy)
        self.update_system_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.update_system_button.setFont(font)
        self.update_system_button.setStyleSheet("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/resource/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_system_button.setIcon(icon8)
        self.update_system_button.setIconSize(QtCore.QSize(60, 60))
        self.update_system_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.update_system_button.setObjectName("update_system_button")
        self.gridLayout_2.addWidget(self.update_system_button, 4, 0, 1, 1)
        self.shut_down_button = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shut_down_button.sizePolicy().hasHeightForWidth())
        self.shut_down_button.setSizePolicy(sizePolicy)
        self.shut_down_button.setMinimumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.shut_down_button.setFont(font)
        self.shut_down_button.setStyleSheet("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/resource/关机.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shut_down_button.setIcon(icon9)
        self.shut_down_button.setIconSize(QtCore.QSize(60, 60))
        self.shut_down_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.shut_down_button.setObjectName("shut_down_button")
        self.gridLayout_2.addWidget(self.shut_down_button, 4, 1, 1, 1)
        self.tabWidget.addTab(self.MainWindow_tab, "")
        self.Position_tab = QtWidgets.QWidget()
        self.Position_tab.setObjectName("Position_tab")
        self.position_table = QtWidgets.QTableWidget(self.Position_tab)
        self.position_table.setGeometry(QtCore.QRect(0, 0, 1001, 551))
        self.position_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.position_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.position_table.setColumnCount(7)
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
        self.measure_table.setGeometry(QtCore.QRect(0, 0, 1011, 551))
        self.measure_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.measure_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.measure_table.setColumnCount(5)
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self._signal_number_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self._signal_number_label.setAutoFillBackground(False)
        self._signal_number_label.setAlignment(QtCore.Qt.AlignCenter)
        self._signal_number_label.setObjectName("_signal_number_label")
        self.horizontalLayout_10.addWidget(self._signal_number_label)
        self.signal_number_combox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.signal_number_combox.setObjectName("signal_number_combox")
        self.signal_number_combox.addItem("")
        self.horizontalLayout_10.addWidget(self.signal_number_combox)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self._signal_structure_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self._signal_structure_label.setAutoFillBackground(False)
        self._signal_structure_label.setAlignment(QtCore.Qt.AlignCenter)
        self._signal_structure_label.setObjectName("_signal_structure_label")
        self.horizontalLayout_5.addWidget(self._signal_structure_label)
        self.signal_structure_combox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.signal_structure_combox.setObjectName("signal_structure_combox")
        self.signal_structure_combox.addItem("")
        self.signal_structure_combox.addItem("")
        self.signal_structure_combox.addItem("")
        self.horizontalLayout_5.addWidget(self.signal_structure_combox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self._work_pattern_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self._work_pattern_label.setAutoFillBackground(False)
        self._work_pattern_label.setObjectName("_work_pattern_label")
        self.horizontalLayout_9.addWidget(self._work_pattern_label, 0, QtCore.Qt.AlignHCenter)
        self.work_pattern_combox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.work_pattern_combox.setObjectName("work_pattern_combox")
        self.work_pattern_combox.addItem("")
        self.work_pattern_combox.addItem("")
        self.horizontalLayout_9.addWidget(self.work_pattern_combox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
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
        self.horizontalLayout_8.addWidget(self.routing_parameters_combox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.line = QtWidgets.QFrame(self.Property_tab)
        self.line.setGeometry(QtCore.QRect(710, 60, 21, 261))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Property_tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(760, 0, 241, 541))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.property_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.property_save_button.sizePolicy().hasHeightForWidth())
        self.property_save_button.setSizePolicy(sizePolicy)
        self.property_save_button.setMinimumSize(QtCore.QSize(90, 90))
        self.property_save_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.property_save_button.setAutoFillBackground(False)
        self.property_save_button.setStyleSheet("")
        self.property_save_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/resource/button_save_juhang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.property_save_button.setIcon(icon10)
        self.property_save_button.setIconSize(QtCore.QSize(90, 90))
        self.property_save_button.setObjectName("property_save_button")
        self.horizontalLayout.addWidget(self.property_save_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabWidget.addTab(self.Property_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.set_property = QtWidgets.QAction(MainWindow)
        self.set_property.setObjectName("set_property")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.__position_label.setText(_translate("MainWindow", "坐标"))
        self._temperature_label.setText(_translate("MainWindow", "温度"))
        self.temperature_show.setText(_translate("MainWindow", "0℃"))
        self.__if_connected_label.setText(_translate("MainWindow", "连通状态"))
        self.__send_rate_main_label_2.setText(_translate("MainWindow", "发送速率"))
        self.__other_equip_ID_label.setText(_translate("MainWindow", "对方设备ID"))
        self.__other_equip_IP_label.setText(_translate("MainWindow", "对方设备IP"))
        self.__not_read_label.setText(_translate("MainWindow", "未读消息个数"))
        self.not_read_count_label.setText(_translate("MainWindow", "0"))
        self.__send_states.setText(_translate("MainWindow", "发送状态"))
        self.send_states_show.setText(_translate("MainWindow", "未接收"))
        self._search_device_label.setText(_translate("MainWindow", "设备搜索 "))
        self.label.setText(_translate("MainWindow", "更新为新功能"))
        self.set_property_button.setText(_translate("MainWindow", "属性配置"))
        self.send_measure_button.setText(_translate("MainWindow", "测量报告"))
        self.start_voice_button.setText(_translate("MainWindow", "语音交互"))
        self.clear_device_button.setText(_translate("MainWindow", "参数清除"))
        self.send_position_button.setText(_translate("MainWindow", "位置报告"))
        self.system_check_button.setText(_translate("MainWindow", "系统自检"))
        self.send_file_button.setText(_translate("MainWindow", "指挥控制"))
        self.reset_button.setText(_translate("MainWindow", "出厂重置"))
        self.update_system_button.setText(_translate("MainWindow", "软件升级"))
        self.shut_down_button.setText(_translate("MainWindow", "关机"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainWindow_tab), _translate("MainWindow", "主界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Position_tab), _translate("MainWindow", "位置数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Measure_tab), _translate("MainWindow", "测量数据"))
        self._signal_number_label.setText(_translate("MainWindow", "信道数"))
        self.signal_number_combox.setItemText(0, _translate("MainWindow", "128"))
        self._signal_structure_label.setText(_translate("MainWindow", "信号体制"))
        self.signal_structure_combox.setItemText(0, _translate("MainWindow", "跳频"))
        self.signal_structure_combox.setItemText(1, _translate("MainWindow", "扩频"))
        self.signal_structure_combox.setItemText(2, _translate("MainWindow", "跳扩"))
        self._work_pattern_label.setText(_translate("MainWindow", "工作模式"))
        self.work_pattern_combox.setItemText(0, _translate("MainWindow", "低速双工(20bps~3840bps)"))
        self.work_pattern_combox.setItemText(1, _translate("MainWindow", "高速双工(38.4kbps~115kbps)"))
        self.__width_band_label.setText(_translate("MainWindow", "频率间隔"))
        self.width_band_combox.setCurrentText(_translate("MainWindow", "225MHz~512MHz"))
        self.width_band_combox.setItemText(0, _translate("MainWindow", "225MHz~512MHz"))
        self.__interval_label.setText(_translate("MainWindow", "信道间隔"))
        self.interval_combox.setItemText(0, _translate("MainWindow", "25kHz"))
        self.interval_combox.setItemText(1, _translate("MainWindow", "625kHz"))
        self.__routing_parameters_label.setText(_translate("MainWindow", "路由协议"))
        self.routing_parameters_combox.setItemText(0, _translate("MainWindow", "OSPF协议"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Property_tab), _translate("MainWindow", "属性"))
        self.set_property.setText(_translate("MainWindow", "属性..."))

import DTresource_rc
