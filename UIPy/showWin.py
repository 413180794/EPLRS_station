# conding:utf-8
import json
import os
import queue
import shutil
import socket
import sys
from datetime import datetime

sys.path.append(os.path.abspath('../tool'))
sys.path.append(os.path.abspath("../Bean"))
sys.path.append(os.path.abspath("../UDPChat"))
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QTimer, QTextStream, QFile
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import QCoreApplication
from ApplyForNetBean import ApplyForNetBean
from NetSuccessBean import NetSuccessBean
from MeasureDataBean import MeasureDataBean
from PositionDataBean import PositionDataBean
from MeasureSuccessReceive import MeasureSuccessReceive
from PositionSuccessReceive import PositionSuccessReceive
from UDPProtocol import UDPProtocol
from mainWindow import Ui_MainWindow
from mylogging import logger
from systemCheck import *
from cat_net import control_net_speed, get_net_data_num, convert_bytes_to_string
from systemInfoDialog import SystemInfoDialog
from ClearSuccessBean import ClearSuccessBean
from ClearDeviceBean import ClearDeviceBean
from ChatDialog import ChatDialog
from VoiceDialog import VoiceDialog
from TimedMBox import TimedMBox
from ApplyForVoiceBean import ApplyForVoiceBean
from RejectVoiceReplyBean import RejectVoiceReplyBean
from AcceptVoiceReplyBean import AcceptVoiceReplyBean


class MainForm(QMainWindow, Ui_MainWindow):
    reply_for_net_failure = pyqtSignal()
    reply_for_net_success = pyqtSignal(bytes)
    not_read_msg_count_signal = pyqtSignal()  # 未读消息计数信号
    position_data_signal = pyqtSignal(bytes, tuple)  # 收到位置数据
    measure_data_signal = pyqtSignal(bytes, tuple)  # 收到测量数据
    clear_device_signal = pyqtSignal(tuple)
    clear_success_signal = pyqtSignal()
    position_recv_signal = pyqtSignal()
    measure_recv_signal = pyqtSignal()
    apply_position_data_signal = pyqtSignal(tuple)
    apply_measure_data_signal = pyqtSignal(tuple)
    apply_voice_signal = pyqtSignal(bytes, tuple)

    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        # self.showFullScreen()
        self.tabWidget.setCurrentWidget(self.MainWindow_tab)  # 先展示出主界面
        self.apply = UDPProtocol(MainForm=self)


        self.init_property()
        self.reply_for_net_success.connect(self.on_reply_for_net_success)
        self.reply_for_net_failure.connect(self.on_reply_for_net_failure)
        self.position_data_signal.connect(self.on_position_data_signal)
        self.measure_data_signal.connect(self.on_measure_data_signal)
        self.position_recv_signal.connect(self.on_position_recv_signal)
        self.measure_recv_signal.connect(self.on_measure_recv_signal)
        self.not_read_msg_count_signal.connect(self.on_not_read_msg_count_signal)
        self.apply_measure_data_signal.connect(self.on_apply_measure_data_signal)
        self.apply_position_data_signal.connect(self.on_apply_position_data_signal)
        with open("device.json", 'r') as f:
            device_config = json.load(f)
        self.device_id = device_config['device_id']
        self.device_category = device_config['device_category']
        self.MYPORT = device_config['my_port']
        self.device_name = self.device_category.split('.')[-1] + "_" + str(self.device_id)
        self.device_ip = self.get_host_ip()
        self.measure_data_path = os.path.join("..", "dataLog", "measure_data.txt")
        self.position_data_path = os.path.join("..", "dataLog", "position_data.txt")
        self.ip_id_table.setHorizontalHeaderLabels(["所属子网","设备类型", "设备ID", "设备IP"])
        self.ip_id_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.position_table.setHorizontalHeaderLabels(["所属子网","设备类型", "设备ID", "设备IP", "经度", "纬度", "高度"])
        self.position_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.measure_table.setHorizontalHeaderLabels(["所属子网","设备类型", '设备ID', '设备IP', '温度'])
        self.measure_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.god_node_addr = (device_config['god_node_ip'], device_config['god_node_port'])  # 上帝节点的地址
        self.not_read_msg_count = 0  # 未读消息计数
        reactor.listenUDP(self.MYPORT, self.apply)
        self.interface = 'eth0'  # 网口名称
        self.property_save_button.clicked.emit()

        self.system_info_dlg = SystemInfoDialog(self)
        self.text_dlg = ChatDialog(self)
        self.voice_dlg = VoiceDialog(self)
        ##################定时查看网卡流量,两次只差计算网速###################

        self.net_data_num_queue = queue.Queue(1)
        self.get_speed_timer = QTimer(self)
        self.get_speed_timer.timeout.connect(self.on_speed_timer)
        self.get_speed_timer.setInterval(5000)
        net_data_num = get_net_data_num(self.interface)
        self.net_data_num_queue.put(net_data_num)
        self.get_speed_timer.start()

        # -----------------------定时查看cpu温度，显示在界面上-----------

        self.get_temperature_timer = QTimer(self)
        self.get_temperature_timer.timeout.connect(self.on_get_temperature_timer)
        self.get_temperature_timer.setInterval(10000)
        self.get_temperature_timer.start()
        # ---------------------------显示经纬度(38.00,23.00)-----------------------------#
        self.position_show.setText("(116.23°,39.54°,12.30km)")
        # 需要删除的对象
        self.clear_success_signal.connect(self.on_clear_success_signal)
        self.clear_device_signal.connect(self.on_clear_device_signal)
        # self.saveImage_path = os.path.join('..', 'saveImage')
        # self.saveImage2_path = os.path.join('..', 'saveImage2')
        self.saveAudio_path = os.path.join('..', 'saveAudio')
        self.dataLog_path = os.path.join('..', 'dataLog')

        self.property_path = os.path.join('property.json')
        self.apply_voice_signal.connect(self.on_apply_voice_signal)



    def on_clear_success_signal(self):
        QMessageBox.critical(self, "结果", "清除成功")

    def on_apply_position_data_signal(self, addr):
        position_x, position_y, position_z = eval(self.position_show.text().replace("°", "").replace("km", ""))
        bean = PositionDataBean(device_category=self.device_category, device_id=self.device_id,
                                position_x=position_x, position_y=position_y, position_z=position_z)
        bean.send(self.apply, addr)
        # 记录发送的位置数据
        with open(self.position_data_path, 'a', encoding='utf-8') as f:
            f.write(
                "EPLRS_NCS apply send position_data-->[{time}]:{self_name}({self_ip})-->{other_name}({other_ip}):   {content}\n".format(
                    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    self_name=self.device_name,
                    self_ip=self.get_host_ip(),
                    other_name="EPLRS_NCS",
                    other_ip=str(addr[0]),
                    content=bean
                )
            )

    @pyqtSlot()
    def on_start_voice_button_clicked(self):
        # print(self.ip_id_table.findItems("mse_t_v",Qt.MatchContains))
        if self.other_equip_ip.text() == "":
            QMessageBox.critical(self, "失败", "请选择对话的对象")
        else:
            if not self.voice_dlg.isVisible():
                self.voice_dlg.device_name_label.setText(self.other_equip_id.text())
                self.voice_dlg.device_ip_label.setText(self.other_equip_ip.text())
                self.voice_dlg.start_voice_button.setVisible(True)
                self.voice_dlg.close_button.setVisible(False)
                self.voice_dlg.show()
                self.voice_dlg.raise_()
                self.voice_dlg.activateWindow()

    @pyqtSlot()
    def on_send_file_button_clicked(self):
        '''
        点击发送文本后触发，生成一个聊天窗口，该窗口很简单，上面显示发送的和接收的文本
        下面为一个输入框，点击发送后将文本发送出去。
        :return:
        '''
        if self.other_equip_ip.text() == "":
            QMessageBox.critical(self, "失败", "请选择发送的对象")
        else:
            self.not_read_msg_count = 0
            self.not_read_count_label.setText(str(self.not_read_msg_count))
            self.text_dlg.my_device_id.setText(str(self.device_name))
            self.text_dlg.my_device_ip.setText(self.device_ip)
            self.text_dlg.other_device_id.setText(self.other_equip_id.text())
            self.text_dlg.other_device_ip.setText(self.other_equip_ip.text())
            self.text_dlg.show()
            self.text_dlg.raise_()
            self.text_dlg.activateWindow()

    def on_apply_measure_data_signal(self, addr):
        bean = MeasureDataBean(device_category=self.device_category, device_id=self.device_id,
                               temperature=float(self.temperature_show.text().replace("℃", "")))
        bean.send(self.apply, addr)
        # 记录发送的测量数据
        with open(self.measure_data_path, 'a', encoding='utf-8') as f:
            f.write(
                "EPLRS_NCS apply send measure_data-->[{time}]:{self_name}({self_ip})-->{other_name}\({other_ip}):   {content}\n".format(
                    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    self_name=self.device_name,
                    self_ip=self.get_host_ip(),
                    other_name="EPLRS_NCS",
                    other_ip=str(addr[0]),
                    content=bean
                )
            )

    def on_clear_device_signal(self, addr):
        '''
        清除参数命令
        :return:
        '''
        try:
            # shutil.rmtree(self.dataLog_path)
            # shutil.rmtree(self.saveImage2_path)
            # shutil.rmtree(self.saveImage_path)
            # shutil.rmtree(self.saveAudio_path)
            os.remove(self.property_path)
            print("清除成功")
        except FileNotFoundError as e:
            print(e)
        else:
            reply = ClearSuccessBean()
            reply.send(self.apply, addr)
            self.close()

    @pyqtSlot()
    def on_clear_device_button_clicked(self):
        # 向选中设备发送清除参数命令
        if self.other_equip_ip.text() == "":
            QMessageBox.critical(self, "失败", "请选择对话的对象")
        else:
            reply = QMessageBox.question(self, "参数清除", "是否确认清除" + str(self.other_equip_id.text()) + "设备的参数",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                return
            elif reply == QMessageBox.Yes:
                clear_msg = ClearDeviceBean()
                print(self.other_equip_ip.text())
                clear_msg.send(self.apply, (self.other_equip_ip.text(), self.MYPORT))

    @pyqtSlot()
    def on_system_check_button_clicked(self):
        '''
        获取自检参数
        :return:
        '''

        self.system_info_dlg.system_info_label.setText(getSystemInfo())
        self.system_info_dlg.cpu_tempe_label.setText(getCPUtemperature())
        self.system_info_dlg.cpu_used_label.setText(getCPUuse())
        self.system_info_dlg.ram_total_label.setText(getRAMinfo("total"))
        self.system_info_dlg.ram_used_label.setText(getRAMinfo("used"))
        self.system_info_dlg.disk_total_label.setText(getDiskSpace("total"))
        self.system_info_dlg.disk_used_label.setText(getDiskSpace("percentage"))
        self.system_info_dlg.voice_card_status_label.setText("正常" if getVoiceCardStatus() is True else "停用")
        self.system_info_dlg.net_card_status_label.setText("正常" if getEthernetAdapterStatus() is True else "停用")
        self.system_info_dlg.show()
        self.system_info_dlg.raise_()
        self.system_info_dlg.activateWindow()

    @pyqtSlot(str)
    def on_search_edit_textEdited(self, text):
        allList = self.ip_id_table.findItems("", Qt.MatchContains)
        for x in allList:
            self.ip_id_table.setRowHidden(x.row(), True)
        qList = self.ip_id_table.findItems(text, Qt.MatchContains)
        for x in qList:
            self.ip_id_table.setRowHidden(x.row(), False)

    def on_position_recv_signal(self):
        self.send_states_show.setText("位置发送成功")

    def on_measure_recv_signal(self):
        self.send_states_show.setText("数据发送成功")

    @pyqtSlot(int)
    def on_tabWidget_tabBarClicked(self, index):

        if 1 <= index <= 2:
            self.not_read_msg_count = 0
            self.not_read_count_label.setText("0")

    def on_position_data_signal(self, datagram: bytes, addr: tuple):
        '''
        收到位置数据
        :param datagram:
        :param add:
        :return:
        '''
        position_bean = PositionDataBean.frombytes(datagram)
        # 记录收到位置数据i
        with open(self.position_data_path, 'a', encoding='utf-8') as f:
            f.write(
                "receive position_data-->[{time}]:{other_name}({other_ip})-->{self_name}({self_ip}):   {content}\n".format(
                    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    other_name=position_bean.device_name,
                    other_ip=str(addr[0]),
                    self_name=self.device_name,
                    self_ip=self.get_host_ip(),
                    content=position_bean
                )
            )
        position_recv_bean = PositionSuccessReceive.frombytes()

        table_item = [QTableWidgetItem(x) for x in
                      [position_bean.ziwang_name,position_bean.device_kind(), position_bean.device_name,
                       addr[0],
                       "{:.3f}°".format(position_bean.position_x),
                       "{:.3f}°".format(position_bean.position_y),
                       "{:.3f}km".format(position_bean.position_z)
                       ]]
        for setItem in table_item:
            setItem.setTextAlignment(Qt.AlignCenter)
            setItem.setToolTip(setItem.text())
        updateList = self.position_table.findItems(position_bean.device_name, Qt.MatchFixedString)

        if len(updateList) == 0:
            self.position_table.insertRow(self.position_table.rowCount())
            for y in range(self.position_table.columnCount()):
                table_item[y].setTextAlignment(Qt.AlignCenter)
                self.position_table.setItem(self.position_table.rowCount() - 1, y, table_item[y])
        else:
            for x in updateList:
                num = x.row()
                for y in range(self.position_table.columnCount()):
                    table_item[y].setTextAlignment(Qt.AlignCenter)
                    self.position_table.setItem(num, y, table_item[y])
        position_recv_bean.send(self.apply, addr)
        self.position_table.scrollToBottom()

    def on_measure_data_signal(self, datagram: bytes, addr: tuple):
        '''
        收到测量数据
        :param datagram:
        :param addr:
        :return:
        '''
        measure_bean = MeasureDataBean.frombytes(datagram)
        # 记录收到的测量数据
        with open(self.measure_data_path, 'a', encoding='utf-8') as f:
            f.write("receive txt-->[{time}]:{other_name}({other_ip})-->{self_name}({self_ip}):   {content}\n".format(
                time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                other_name=measure_bean.device_name,
                other_ip=str(addr[0]),
                self_name=self.device_name,
                self_ip=self.get_host_ip(),
                content=measure_bean
            )
            )
        measure_recv_bean = MeasureSuccessReceive.frombytes()
        table_item = [QTableWidgetItem(x) for x in
                      [measure_bean.ziwang_name,measure_bean.device_kind(), measure_bean.device_name,
                       addr[0],
                       str(measure_bean.temperature) + "℃"]]
        for setItem in table_item:
            setItem.setTextAlignment(Qt.AlignCenter)
            setItem.setToolTip(setItem.text())
        updateList = self.measure_table.findItems(measure_bean.device_name, Qt.MatchFixedString)

        if len(updateList) == 0:
            self.measure_table.insertRow(self.measure_table.rowCount())
            for y in range(self.measure_table.columnCount()):
                table_item[y].setTextAlignment(Qt.AlignCenter)
                self.measure_table.setItem(self.measure_table.rowCount() - 1, y, table_item[y])
        else:
            for x in updateList:
                num = x.row()
                for y in range(self.measure_table.columnCount()):
                    table_item[y].setTextAlignment(Qt.AlignCenter)
                    self.measure_table.setItem(num, y, table_item[y])
        measure_recv_bean.send(self.apply, addr)
        self.measure_table.scrollToBottom()

    def on_speed_timer(self):
        '''
        根据self.interface的网卡流量来计算当前的网速
        :return:
        '''
        net_data_num = get_net_data_num(self.interface)
        if net_data_num is None:
            self.send_rate_show.setText("未连接")
            if self.interface == "eth0":
                self.interface = 'wlan0'
            elif self.interface == "wlan0":
                self.interface = 'eth0'
        elif self.net_data_num_queue.full():
            old_net_data_num = self.net_data_num_queue.get()
            download_speed = (float(net_data_num) - float(old_net_data_num))
            download_speed_str = convert_bytes_to_string(download_speed)
            self.send_rate_show.setText(download_speed_str + "/s")
            self.net_data_num_queue.put(net_data_num)

    def on_get_temperature_timer(self):
        '''
        树莓派中获取cpu温度
        :return:
        '''

        self.temperature_show.setText(getCPUtemperature())

    @pyqtSlot()
    def on_send_measure_button_clicked(self):
        '''
        向选中的设备发送测量数据
        :return:
        '''
        if self.other_equip_ip.text() == "" or self.other_equip_ip.text() == "未连接":
            QMessageBox.critical(self, "失败", "请选择报告的对象")
        else:
            _temperature = self.temperature_show.text()
            if _temperature == "":
                self.send_states_show.setText("未接收")
                return
            bean = MeasureDataBean(device_category=self.device_category, device_id=self.device_id,
                                   temperature=float(self.temperature_show.text().replace("℃", "")))
            bean.send(self.apply, (self.other_equip_ip.text().strip(), self.MYPORT))
            # 记录发送的测量数据
            with open(self.measure_data_path, 'a', encoding='utf-8') as f:
                f.write(
                    "send measure_data-->[{time}]:{self_name}({self_ip})-->{other_name}({other_ip}):   {content}\n".format(
                        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        self_name=self.device_name,
                        self_ip=self.get_host_ip(),
                        other_name=self.other_equip_id.text(),
                        other_ip=self.other_equip_ip.text(),
                        content=bean
                    )
                )
            self.send_states_show.setText("未接收")

    @pyqtSlot()
    def on_send_position_button_clicked(self):
        '''
        向选中的设备发送位置数据
        :return:
        '''
        if self.other_equip_ip.text() == "" or self.other_equip_ip.text() == "未连接":
            QMessageBox.critical(self, "失败", "请选择报告的对象")
        else:
            position_x, position_y, position_z = eval(self.position_show.text().replace("°", "").replace("km", ""))

            print(self.device_category)
            bean = PositionDataBean(device_category=self.device_category, device_id=self.device_id,
                                    position_x=position_x, position_y=position_y, position_z=position_z)
            bean.send(self.apply, (self.other_equip_ip.text().strip(), self.MYPORT))
            # 记录发送的位置数据
            with open(self.position_data_path, 'a', encoding='utf-8') as f:
                f.write(
                    "send   position_data-->[{time}]:{self_name}({self_ip})-->{other_name}({other_ip}):   {content}\n".format(
                        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        self_name=self.device_name,
                        self_ip=self.get_host_ip(),
                        other_name=self.other_equip_id.text(),
                        other_ip=self.other_equip_ip.text(),
                        content=bean
                    )
                )
            self.send_states_show.setText("未接收")

    def closeEvent(self, QCloseEvent):
        QCoreApplication.instance().quit()
        # QCloseEvent.accept()

    def on_not_read_msg_count_signal(self):
        '''
        每次收到新的消息都会触发这个函数，此函数目的是对未读消息进行计数，默认如果用户
        打开了text_dlg，那么就认为用户读取了所有消息。如果用户没有打开text_dlg，就
        将未读消息加一
        :return:
        '''
        if self.Position_tab.isVisible() or self.Measure_tab.isVisible() or self.text_dlg.isVisible():
            # 如果聊天框被打开，新的数据上来，什么都不用干
            pass
        else:
            # 如果聊天框没有被打开，新的数据上来，将未读数据加一
            self.not_read_msg_count += 1
            self.not_read_count_label.setText(str(self.not_read_msg_count))

    @pyqtSlot(int, int)
    def on_ip_id_table_cellClicked(self, row, colmn):
        '''
        对点击ip_id_table做出响应，思路，点击某一行，将这一行的ip显示到右侧
        :param row:
        :param colmn:
        :return:
        '''
        device_ip = self.ip_id_table.item(row, 3).text()  # 获得该行中的ip地址
        device_id = self.ip_id_table.item(row, 2).text()  # 获得该行中的i
        self.other_equip_id.setText(device_id)
        self.other_equip_ip.setText(device_ip)

        # bean = ApplyPosition()
        # bean.send(self.apply,(self.other_equip_ip.text().strip(), self.MYPORT))

    def ip_id_list_to_many_one_line(self, ip_comma_interval):
        '''
        '127.0.0.0:sdd_MSE_t,123.2.1.2:sf_MSE_t' --- > yield [TableWidget(id),TableWidget(ip)]
        :param ip_comma_interval:
        :return:
        '''
        ip_id_list = str(ip_comma_interval).split(",")
        for ip_id in ip_id_list:
            ip = ip_id.split(":")[0]
            id = ip_id.split(":")[1].split('.')[-1]
            ziwang = ip_id.split(":")[1].split(".")[-2]
            id_item = QTableWidgetItem(id)
            ip_item = QTableWidgetItem(ip)
            ziwang_item = QTableWidgetItem(ziwang)
            if ziwang == "Real":
                kind = "模拟电台"
            else:
                kind = "虚拟电台"
            kind_item = QTableWidgetItem(kind)
            yield [ziwang_item,kind_item, id_item, ip_item]

    def insert_data_to_ip_id_table(self, data):
        '''
        将data插入至表格，Data的形式为 [设备ID，设备IP]表示了一行
        :param result:
        :return:
        '''
        self.ip_id_table.insertRow(self.ip_id_table.rowCount())
        for y in range(self.ip_id_table.columnCount()):
            self.ip_id_table.setItem(self.ip_id_table.rowCount() - 1, y, data[y])
            self.ip_id_table.scrollToBottom()

    def clear_table_data(self):
        '''
            清空表格中的所有数据
        :return:　ｎｏｎｅ
        '''
        self.ip_id_table.setRowCount(0)  # 清空所有行
        self.ip_id_table.clearContents()  # 清空所有内容

    def on_reply_for_net_success(self, datagram):
        '''
        入网成功之后，将收到的"127.0.0.1:sdf_MSE_t,"123.1.2.3:sd_MSE_t"
        显示在表格中，清空原有的数据，填充新收到的数据
        :param ip_comma_interval:
        :return:
        '''
        reply_for_net_success_obj = NetSuccessBean.frombytes(datagram)
        ip_comma_interval = reply_for_net_success_obj.ip_list
        for data in self.ip_id_list_to_many_one_line(ip_comma_interval):
            for setdata in data:
                setdata.setTextAlignment(Qt.AlignCenter)
                setdata.setToolTip(setdata.text())
            self.insert_data_to_ip_id_table(data)
        self.if_connected_main.setText("成功入网")
        # QMessageBox.about(self, "入网成功", "入网成功")

    def on_reply_for_net_failure(self):
        '''
        入网失败之后，提示入网失败
        :return: None
        '''
        self.if_connected_main.setText("未连接")
        QMessageBox.critical(self, "入网失败", "请正确设置设备属性，或联系网络管理员")
        self.clear_table_data()

    def on_connect_refused(self):
        QMessageBox.critical(self, "入网申请错误", "请检查网络连接")

    # 绑定滚动dial
    # def send_rate_dial_valueChanged(self):
    #     self.send_rate_spinbox.setValue(self.send_rate_dial.value())

    # 申请入网 属性配置 只需要 width_band interval routing_parameters
    def init_property(self):
        '''
        读取现有的property.json文件中的设备属性，并显示在界面中
        :return: None
        '''
        if os.path.exists("property.json"):
            with open("property.json", "r") as f:
                property_json = json.load(f)
                assert type(property_json) == dict
            for key, name in property_json.items():
                getattr(getattr(self, key + "_combox"), "setCurrentText")(name)
        else:
            raise Exception

    @pyqtSlot()
    def on_property_save_button_clicked(self):
        '''
        绑定保存按钮
        :return:
        '''
        # 如果需要添加属性，在property_json直接添加就可以了
        if self.work_pattern_combox.currentText() == "高速双工":
            control_net_speed(self.interface,"115kbit")
        elif self.work_pattern_combox.currentText() == "低速双工":
            control_net_speed(self.interface,"3.84kbit")
        property_json = {
            "width_band": self.width_band_combox.currentText(),
            "interval": self.interval_combox.currentText(),
            "routing_parameters": self.routing_parameters_combox.currentText()
        }
        self.save_property_json(property_json)
        self.send_property(property_json)

        self.tabWidget.setCurrentWidget(self.MainWindow_tab)
        # 数据的顺序以此是width_band,interval,schedule,routing_parameters,type,ip_id_list.入网申请的时候ip_id_list为空
        # 也就只给ip_id_list分配了一个字节

    def save_property_json(self, property_json):
        '''
        将property_json保存到文件中
        :param property_json:
        :return:
        '''
        with open("property.json", 'w', encoding='utf-8') as f:
            json.dump(property_json, f)

    def send_property(self, property_json):
        '''
        将property_json中的数据发送至上帝节点
        :param property_json:
        :return:
        '''
        # 该函数将property_json中的值进行打包，所有字节都是16个字节。json的长度可变
        width_band = {"225MHz~512MHz": 1}
        interval = {"625kHz": 625, "25kHz": 25}
        apply_for_net_obj = ApplyForNetBean(
            width_band=width_band.get(property_json.get("width_band")),
            interval=interval.get(property_json.get("interval")),
            routing_parameter=property_json.get("routing_parameters"),
            device_id=self.device_id,
            device_category=self.device_category
        )
        apply_for_net_obj.send(self.apply, self.god_node_addr)
        self.clear_table_data()
        # self.apply.send_apply(apply_for_net_obj.pack_data, ("127.0.0.1", 10000))
        # 这里搞成applyforobj自己的属性。他可以实现自己发送 发送文本

    @pyqtSlot()
    def on_set_property_button_clicked(self):
        '''
        点击入网申请后，跳转至主页面
        :return:
        '''
        self.tabWidget.setCurrentWidget(self.Property_tab)
        # self.send_text_button

    def on_apply_voice_signal(self, datagram, addr):
        '''
        一切的起始点都要从voicedialog的状态是等待拨号，只有在该状态下，才可以接收别人的请求通话命令
        如果其他请求通话时候，状态不是等待拨号，说明voicedialog正在通话中，返回拒绝通话命令（考虑正在通话命令）
        :return:
        '''
        self.other_addr = addr
        if self.voice_dlg.status_label.text() == "等待拨号":
            # 如果状态是等待拨号，收到请求通话命令后，状态切换为正在建立连接，并创建回调，10秒后判断状态是否
            # 仍然是正在建立连接，如果是，返回拒绝通话，并且挂断。
            apply_voice_bean = ApplyForVoiceBean.frombytes(datagram)
            self.voice_dlg.status_label.setText('正在建立连接')
            self.voice_dlg.start_voice_button.setVisible(False)
            self.voice_dlg.close_button.setVisible(True)
            self.voice_dlg.device_name_label.setText(apply_voice_bean.device_name)
            self.voice_dlg.device_ip_label.setText(addr[0])
            self.voice_dlg.show()
            self.voice_dlg.raise_()
            self.voice_dlg.activateWindow()
            result = TimedMBox.question(title="请求通话", text=apply_voice_bean.device_name+ "请求通话" + "\n" + "是否同意？")

            # 上述会定时10秒
            # result = QMessageBox.question(self.voice_dlg,
            #                               "请求通话",
            #                               apply_voice_bean.device_category + "_" + str(
            #                                   apply_voice_bean.device_id) + "请求通话" + "\n" + "是否同意？",
            #                               QMessageBox.Yes | QMessageBox.No)
            if result == QMessageBox.Yes:
                # 如果同意对方的回答，那么就要开始向对象发送语音，弹出voiceDialog，发送语音的任务交给voiceDialog
                accept_voice_reply_bean = AcceptVoiceReplyBean()
                accept_voice_reply_bean.send(self.apply, addr)



            elif result == QMessageBox.No:
                # 　如果不同意通话，返回拒绝通话命令,并且挂断
                reject_voice_reply_bean = RejectVoiceReplyBean()
                reject_voice_reply_bean.send(self.apply, addr)
                self.voice_dlg.close()
        else:
            # 如果状态不是 等待拨号，说明该设备正在通话中或者正在建立通话中，直接返回拒绝通话
            reject_voice_reply_bean = RejectVoiceReplyBean()
            reject_voice_reply_bean.send(self.apply, addr)

    def get_host_ip(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except Exception as e:
            logger.error(e)
            return '0.0.0.0'
        finally:
            s.close()
        return ip

    @pyqtSlot()
    def on_reset_button_clicked(self):
        reply = QMessageBox.question(self, "参数清除", "是否确认回复出厂设置",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
        elif reply == QMessageBox.Yes:
            self.interval_combox.setCurrentIndex(0)
            self.routing_parameters_combox.setCurrentIndex(0)
            self.width_band_combox.setCurrentIndex(0)
            self.signal_number_combox.setCurrentIndex(0)
            self.signal_structure_combox.setCurrentIndex(0)
            self.work_pattern_combox.setCurrentIndex(0)
            shutil.rmtree(self.dataLog_path)
            shutil.rmtree(self.saveAudio_path)
            os.mkdir(self.dataLog_path)
            os.mkdir(self.saveAudio_path)

    @pyqtSlot()
    def on_update_system_button_clicked(self):
        reply = QMessageBox.question(self, "参数清除", "是否确认升级软件",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
        elif reply == QMessageBox.Yes:
            os.chdir("..")
            os.popen("git fetch --all")
            os.popen("git reset --hard origin/master")
            x = os.popen("git pull").read()
            os.chdir("./UIPy")
            QMessageBox.critical(self, "升级信息", x)


def getstylesheetfromQss(qss_path):
    file = QFile(qss_path)
    file.open(QFile.ReadOnly)
    ts = QTextStream(file)
    stylesheet = ts.readAll()
    return stylesheet

if __name__ == '__main__':
    app = QApplication(sys.argv)
    import qt5reactor

    qt5reactor.install()
    from twisted.internet import reactor

    reactor.suggestThreadPoolSize(30)
    win = MainForm()
    stylesheet = getstylesheetfromQss('../Qss/Dark/darkstyle.qss')
    win.setStyleSheet(stylesheet)
    win.voice_dlg.setStyleSheet(stylesheet)
    win.text_dlg.setStyleSheet(stylesheet)
    win.system_info_dlg.setStyleSheet(stylesheet)

    win.show()
    reactor.run()
