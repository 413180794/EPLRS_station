# conding:utf-8
import json
import os
import queue
import socket
import sys
from datetime import datetime

sys.path.append(os.path.abspath('../tool'))
sys.path.append(os.path.abspath("../Bean"))
sys.path.append(os.path.abspath("../UDPChat"))
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QTimer
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
from property import Property
from systemCheck import getCPUtemperature, getSystemInfo, getCPUuse, getRAMinfo, getDiskSpace, getVoiceCardStatus, \
    getEthernetAdapterStatus
from cat_net import get_net_data_num, convert_bytes_to_string
from systemInfoDialog import SystemInfoDialog
from ClearSuccessBean import ClearSuccessBean
from ClearDeviceBean import ClearDeviceBean


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

    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentWidget(self.MainWindow_tab)  # 先展示出主界面
        self.apply = UDPProtocol(MainForm=self)
        self.MYPORT = 10001  # 其他节点默认端口
        reactor.listenUDP(self.MYPORT, self.apply)
        self.init_property()
        self.send_rate_dial.valueChanged.connect(self.send_rate_dial_valueChanged)  # 奇怪，使用装饰器绑定不到，是库的bug么
        self.send_rate_spinbox.valueChanged.connect(self.send_rate_spinbox_valueChanged)
        self.reply_for_net_success.connect(self.on_reply_for_net_success)
        self.reply_for_net_failure.connect(self.on_reply_for_net_failure)
        self.position_data_signal.connect(self.on_position_data_signal)
        self.measure_data_signal.connect(self.on_measure_data_signal)
        self.position_recv_signal.connect(self.on_position_recv_signal)
        self.measure_recv_signal.connect(self.on_measure_recv_signal)
        self.not_read_msg_count_signal.connect(self.on_not_read_msg_count_signal)
        self.device_id = 0
        self.device_category = "eplrs_t_r"
        self.device_name = self.device_category + "_" + str(self.device_id)
        self.device_ip = self.get_host_ip()
        self.measure_data_path = os.path.join("..", "dataLog", "measure_data.txt")
        self.position_data_path = os.path.join("..", "dataLog", "position_data.txt")
        self.ip_id_table.setHorizontalHeaderLabels(["设备类型", "设备ID", "设备IP"])
        self.ip_id_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.position_table.setHorizontalHeaderLabels(["设备类型", "设备ID", "设备IP", "经度", "维度"])
        self.position_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.measure_table.setHorizontalHeaderLabels(["设备类型", '设备ID', '设备IP', '测量数据'])
        self.measure_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.god_node_addr = ('127.0.0.1', 10000)  # 上帝节点的地址
        self.not_read_msg_count = 0  # 未读消息计数
        self.property_save_button.clicked.emit()
        self.system_info_dlg = SystemInfoDialog(self)
        ##################定时查看网卡流量,两次只差计算网速###################
        self.interface = 'eth1'  # 网口名称
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
        self.position_show.setText("(116.23,39.54)")
        # 需要删除的对象
        self.clear_success_signal.connect(self.on_clear_success_signal)
        self.clear_device_signal.connect(self.on_clear_device_signal)
        # self.saveImage_path = os.path.join('..', 'saveImage')
        # self.saveImage2_path = os.path.join('..', 'saveImage2')
        # self.saveAudio_path = os.path.join('..', 'saveAudio')
        self.dataLog_path = os.path.join('..', 'dataLog')

    def on_clear_success_signal(self):
        QMessageBox.critical(self, "结果", "清除成功")

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
            print("清除成功")
        except FileNotFoundError as e:
            print(e)
        else:
            reply = ClearSuccessBean()
            reply.send(self.apply, addr)

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
        # 记录收到位置数据
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
        self.position_table.insertRow(self.position_table.rowCount())
        table_item = [QTableWidgetItem(x) for x in
                      [position_bean.device_kind(), position_bean.device_category + "_" + str(position_bean.device_id),
                       addr[0],
                       str(position_bean.position_x),
                       str(position_bean.position_y)]]
        for y in range(self.position_table.columnCount()):
            table_item[y].setTextAlignment(Qt.AlignCenter)
            self.position_table.setItem(self.position_table.rowCount() - 1, y, table_item[y])
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
        self.measure_table.insertRow(self.measure_table.rowCount())
        table_item = [QTableWidgetItem(x) for x in
                      [measure_bean.device_kind(), measure_bean.device_category + "_" + str(measure_bean.device_id),
                       addr[0],
                       str(measure_bean.temperature)]]
        for y in range(self.measure_table.columnCount()):
            table_item[y].setTextAlignment(Qt.AlignCenter)
            self.measure_table.setItem(self.measure_table.rowCount() - 1, y, table_item[y])
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
            if self.interface == "eth1":
                self.interface = 'wlan0'
            elif self.interface == "wlan0":
                self.interface = 'eth1'
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
            position_x = eval(self.position_show.text())[0]
            position_y = eval(self.position_show.text())[1]
            bean = PositionDataBean(device_category=self.device_category, device_id=self.device_id,
                                    position_x=position_x, position_y=position_y)
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
        if self.Position_tab.isVisible() or self.Measure_tab.isVisible():
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
        device_ip = self.ip_id_table.item(row, 2).text()  # 获得该行中的ip地址
        device_id = self.ip_id_table.item(row, 1).text()  # 获得该行中的i
        self.other_equip_id.setText(device_id)
        self.other_equip_ip.setText(device_ip)

    def ip_id_list_to_many_one_line(self, ip_comma_interval):
        '''
        '127.0.0.0:sdd_MSE_t,123.2.1.2:sf_MSE_t' --- > yield [TableWidget(id),TableWidget(ip)]
        :param ip_comma_interval:
        :return:
        '''
        ip_id_list = str(ip_comma_interval).split(",")
        for ip_id in ip_id_list:
            ip = ip_id.split(":")[0]
            id = ip_id.split(":")[1]
            id_item = QTableWidgetItem(id)
            ip_item = QTableWidgetItem(ip)
            id_item.setTextAlignment(Qt.AlignCenter)
            ip_item.setTextAlignment(Qt.AlignCenter)
            if "r" == id.split("_")[-2]:
                kind = "模拟电台"
            else:
                kind = "虚拟电台"
            kind_item = QTableWidgetItem(kind)
            kind_item.setTextAlignment(Qt.AlignCenter)
            yield [kind_item, id_item, ip_item]

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

    def send_rate_spinbox_valueChanged(self):
        '''
        dial与spinbox绑定
        :return:
        '''
        self.send_rate_dial.setValue(int(self.send_rate_spinbox.value()))

    def on_connect_refused(self):
        QMessageBox.critical(self, "入网申请错误", "请检查网络连接")

    # 绑定滚动dial
    def send_rate_dial_valueChanged(self):
        self.send_rate_spinbox.setValue(self.send_rate_dial.value())

    # 申请入网 属性配置 只需要 width_band interval routing_parameters
    def init_property(self):
        '''
        读取现有的property.json文件中的设备属性，并显示在界面中
        :return: None
        '''
        if os.path.exists("property.json"):
            with open("property.json", "r") as f:
                property_json = json.load(f)
                property_obj = Property(
                    width_band=property_json.get("width_band"),
                    interval=property_json.get("interval"),
                    routing_parameters=property_json.get("routing_parameters")
                )
            for name in property_obj.__slots__:
                # 一行代替以下所有的代码，getattr(self,name+"_combox") == self.xxx_combox
                # getattr(getattr(self,name+"_combox),"setCurrentText) == self.xxx_combox.setCurrent
                # getattr(self.property_obj,name) == property_obj.xxxx
                getattr(getattr(self, name + "_combox"), "setCurrentText")(getattr(property_obj, name))

    @pyqtSlot()
    def on_property_save_button_clicked(self):
        '''
        绑定保存按钮
        :return:
        '''
        # 如果需要添加属性，在property_json直接添加就可以了
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
        width_band = {"30MHz~90MHz": 1, "610MHz~690MHz": 2, "225MHz~512MHz": 4, "1350MHz~1850MHz": 8}
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    import qt5reactor

    qt5reactor.install()
    from twisted.internet import reactor

    win = MainForm()
    win.show()
    reactor.run()
