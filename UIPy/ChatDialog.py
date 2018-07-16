import shutil
from datetime import datetime
import hashlib
import threading
import time

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox
import os
import sys

sys.path.append(os.path.abspath("../Bean"))
# from PicDataBean import PicDataBean
# from PicSuccessReceiveBean import PicSuccessReceiveBean
from TextDataBean import TextDataBean
from TextSuccessReceive import TextSuccessReceive
from chatWindows import Ui_Dialog
from msgList import MsgList
from mylogging import logger


class ChatDialog(QDialog, Ui_Dialog):
    text_data_signal = pyqtSignal(bytes, tuple)  # 发送而来的文本数据信号
    # pic_data_signal = pyqtSignal(bytes, tuple)  # 发送而来的图片数据信号
    text_data_receive_signal = pyqtSignal()  # 对方成功接收文本信号
    # pic_data_receive_signal = pyqtSignal()  # 对方成功接收图像信号
    change_other_ip_id_signal = pyqtSignal(str, str)

    IMAGE_PATH = '../saveImage'

    def __init__(self, MainForm=None):
        super(ChatDialog, self).__init__()
        self.setupUi(self)
        self.MainForm = MainForm
        self.text_data_signal.connect(self.on_text_data_signal)  # 收到文本的信号
        # self.pic_data_signal.connect(self.on_pic_data_signal)  # 收到图像的信号
        self.change_other_ip_id_signal.connect(self.on_change_other_ip_id)  # 为了实现双击聊天框，将对方的ip id放入到左侧
        self.text_data_receive_signal.connect(self.on_text_data_receive_signal)  # 得知对方已经收到发出的文本
        # self.pic_data_receive_signal.connect(self.on_pic_data_receive_signal)  # 得知对方已经收到发出的图像
        self.chat_log_path = os.path.join("..","dataLog","chat.txt")
        # self.pic_log_path = os.path.join("..","dataLog","piclog.txt")
        # self.image_save_path = os.path.join("..","saveImage2")
        # self.max_pic_size = 1024
        # self.pic_data_dict = {}  # 存放每一个文件的数据，用于解决接收udp顺序错误问题

    def on_change_other_ip_id(self, ip, device_name):
        self.other_device_ip.setText(ip)
        self.other_device_id.setText(device_name)

    def on_text_data_receive_signal(self):
        self.if_receive_msg.setText("文本接收成功")

    # def on_pic_data_receive_signal(self):
    #     self.if_receive_msg.setText("图片接收成功")

    @pyqtSlot()
    def on_close_button_clicked(self):
        '''https://www.teamviewer.com/zhcn/download/linux
        绑定关闭按钮
        :return:
        '''
        self.close()
    @pyqtSlot()
    def on_turn_about_order_button_clicked(self):
        self.textEdit.setText("向后转！")
        self.send_msg_button.clicked.emit()

    @pyqtSlot()
    def on_turn_left_order_button_clicked(self):
        self.textEdit.setText("向左转！")
        self.send_msg_button.clicked.emit()
    @pyqtSlot()
    def on_turn_right_order_button_clicked(self):
        self.textEdit.setText("向右转！")
        self.send_msg_button.clicked.emit()
    @pyqtSlot()
    def on_forward_order_button_clicked(self):
        self.textEdit.setText("前进！")
        self.send_msg_button.clicked.emit()
        
    @pyqtSlot()
    def on_send_msg_button_clicked(self):
        '''
        绑定发送消息按钮，需要做
        1.获取文本框的输入
        2.形成TextBean
        3.清空文本框
        4.展示 xxx：  输入内容
        5.发送出去

        :return:
        '''
        self.if_receive_msg.setText('未接收')
        msg = self.textEdit.document().toPlainText()  # 获取文本框的输入
        if msg.strip() == "":
            return
        msg_bean = TextDataBean(device_category=self.MainForm.device_category,
                                device_id=self.MainForm.device_id,
                                data=msg
                                )  # 形成TextBean
        self.textEdit.document().clear()
        self.listWidget.addTextMsg(self.MainForm.device_name, msg, False, ip=self.MainForm.get_host_ip())
        msg_bean.send(self.MainForm.apply, (self.other_device_ip.text().strip(), self.MainForm.MYPORT))
        with open(self.chat_log_path, 'a',encoding='utf-8') as f:
            f.write("send    txt-->[{time}]:{self_name}({self_ip})-->{other_name}({other_ip}):   {content}\n".format(
                time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                self_name=self.my_device_id.text(),
                self_ip=self.my_device_ip.text(),
                other_name=self.other_device_id.text(),
                other_ip=self.other_device_ip.text(),
                content=msg_bean.data
            )
            )

    # def get_md5_of_file(self, fname):
    #     '''
    #     输入文件路径，返回该文件的md5值
    #     如果该文件不存在，则返回None,
    #     采用更新的方式，避免大文件内存溢出
    #     :param fname:
    #     :return:
    #     '''
    #     if not os.path.exists(fname):
    #         return None
    #     with open(fname, 'rb') as f:
    #         m = hashlib.md5()
    #         while True:
    #             d = f.read(10240)
    #             if not d:
    #                 break
    #             m.update(d)
    #     return m.hexdigest()
    #
    # def get_file_size(self, fname):
    #     '''
    #     传入文件路径，返回该文件的大小,
    #     如果文件不存在，则返回NOne
    #     :param fname:
    #     :return:
    #     '''
    #     if not os.path.exists(fname):
    #         return None
    #     return os.path.getsize(fname)
    #
    # def get_file_ext(self, fname):
    #     filepath, tempfilename = os.path.split(fname)
    #     shotname, extension = os.path.splitext(tempfilename)
    #     return extension
    #
    # @pyqtSlot()
    # def on_send_pic_button_clicked(self):
    #     '''
    #
    #     :return:
    #     '''
    #     self.if_receive_msg.setText("未接收")
    #     file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", '/', "Images (*.png *.jpg *.bmp *.jpeg)")
    #     print(file_name)
    #
    #     file_ext = self.get_file_ext(file_name)
    #     print(file_ext)
    #     if file_name is "":
    #         return
    #
    #     self.listWidget.addImageMsg(self.MainForm.device_name, file_name, False, ip=self.MainForm.get_host_ip())
    #     md_5 = self.get_md5_of_file(file_name)  # 获得该文件的md5值。
    #     if md_5 is None:  # 如果该文件不存在，给予提示，但基本不会不存在的。
    #         QMessageBox.critical(self, "文件不存在", "文件不存在")
    #     file_size_all = self.get_file_size(file_name)  # 取得文件整体大小
    #
    #     data_nums = int(file_size_all / self.max_pic_size) + 1  # 将file分成data_nums份
    #     print("data_nums:" + str(data_nums))
    #
    #     def send_pic():
    #         with open(file_name, 'rb') as f:
    #             for data_num in range(0, data_nums):
    #                 data = f.read(self.max_pic_size)
    #                 file_size = len(data)  # 当前读取出来的大小
    #                 pic_bean = PicDataBean(file_ext=file_ext, md_5=md_5, device_category=self.MainForm.device_category,
    #                                        device_id=self.MainForm.device_id, size=file_size,
    #                                        data_nums=data_nums, data_num=data_num, data=data)
    #
                    # self.send_pic_signal.emit(pic_bean)
                    # if self.if_receive_msg.text().strip() == '未接收':
                    #     time.sleep(0.01)
                    #     pic_bean.send(self.MainForm.apply, (self.other_device_ip.text().strip(), self.MainForm.MYPORT))
            #
            # print('sendpic')
            # with open(self.pic_log_path, 'a',encoding='utf-8') as f:
            #     f.write(
            #         "send    pic-->[{time}]:{self_name}({self_ip})-->{other_name}({other_ip}):   {content}\n".format(
            #             time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            #             self_name=self.my_device_id.text(),
            #             self_ip=self.my_device_ip.text(),
            #             other_name=self.other_device_id.text(),
            #             other_ip=self.other_device_ip.text(),
            #             content=file_name
            #         )
            #     )
        #
        # t = threading.Thread(target=send_pic)
        # t.start()
    #

    def on_text_data_signal(self, datagram, addr):
        '''
        收到对方发送而来的信息需要做，
        1.通过信号把datagram发送到showDialog
        2.将datagram形成bean
        3.将msg显示在界面中。
        4.
        5.给对面回复 我已经收到
        :param msg:
        :return:
        '''
        text_data_obj = TextDataBean.frombytes(datagram)
        assert type(text_data_obj.data) == str
        self.MainForm.other_equip_ip.setText(str(addr[0]))
        self.MainForm.other_equip_id.setText(text_data_obj.device_name)
        self.listWidget.addTextMsg(text_data_obj.device_name, text_data_obj.data, True, ip=str(addr[0]))
        with open(self.chat_log_path, 'a',encoding='utf-8') as f:
            f.write("receive txt-->[{time}]:{other_name}({other_ip})-->{self_name}({self_ip}):   {content}\n".format(
                time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                other_name=text_data_obj.device_name,
                other_ip=str(addr[0]),
                self_name=self.MainForm.device_name,
                self_ip=self.MainForm.get_host_ip(),
                content=text_data_obj.data
            )
        )
        text_success_receive_bean = TextSuccessReceive()
        text_success_receive_bean.send(self.MainForm.apply, addr)

    # def on_pic_data_signal(self, datagram, addr):
    #     通过bean自身保存到文件
    #     要解决数据不按顺序来的问题。
        # bean = PicDataBean.frombytes(datagram)
        # print(bean.data_nums)
        # print(bean.data_num)
        # print(len(bean.data))
        # 先判断该图片有没有接收过。
        # if os.path.exists(os.path.join(self.IMAGE_PATH, bean.md_5 + bean.file_ext)):
        #     如果以前收到过，直接存，不用在收了。\
            #
            # print("已经有了")
            # if bean.data_num == 1:
            #     with open(self.pic_log_path, 'a',encoding='utf-8') as f:
            #         f.write(
            #             "receive pic-->[{time}]:{other_name}({other_ip})-->{self_name}({self_ip}):   {content}\n".format(
            #                 time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            #                 other_name=bean.device_name(),
            #                 other_ip=str(addr[0]),
            #                 self_name=self.my_device_id.text(),
            #                 self_ip=self.my_device_ip.text(),
            #                 content=bean.md_5 + bean.file_ext
            #             ))
            #     shutil.copyfile(os.path.join(self.IMAGE_PATH, bean.md_5 + bean.file_ext),
            #                     os.path.join(self.image_save_path, "{time}_{other_name}_{other_ip}{file_ext}".format(
            #                         time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            #                         other_name=bean.device_name(),
            #                         other_ip=str(addr[0]),
            #                         file_ext=bean.file_ext
            #                     )))
            #     self.listWidget.addImageMsg(self.MainForm.device_name,
            #                                 os.path.join(self.IMAGE_PATH, bean.md_5 + bean.file_ext), True,
            #                                 ip=str(addr[0]))
            #     self.MainForm.not_read_msg_count_signal.emit()
            #     pic_success_receive_bean = PicSuccessReceiveBean()
            #     pic_success_receive_bean.send(self.MainForm.apply, addr)
            # return
        #
        # if not self.pic_data_dict.get(bean.md_5):
        #     如果事前没有,创建数组
            # self.pic_data_dict[bean.md_5] = []
        # print(bean.data_num)
        # self.pic_data_dict.get(bean.md_5).insert(bean.data_num, bean.data)  # 按照序号添加
        # 　判断是否已经接收完毕
        # print(self.pic_data_dict)
        # print("长度"+str(len(self.pic_data_dict.get(bean.md_5))))
        # if bean.data_num == bean.data_nums-1:
        #
        #     print(os.path.join(self.IMAGE_PATH,bean.md_5+bean.file_ext))
        #     with open(os.path.join(self.IMAGE_PATH, bean.md_5 + bean.file_ext), 'ab') as f:
        #         for data in self.pic_data_dict.get(bean.md_5):
        #             f.write(data)
        #         logger.info('收完')
        #
        #     self.pic_data_dict.pop(bean.md_5)
        #     md_5 = self.get_md5_of_file(os.path.join(self.IMAGE_PATH, bean.md_5 + bean.file_ext))  # 获得该文件的md5值。
        #     print(md_5)
        #     print(bean.md_5)
        #     if md_5 == bean.md_5:
        #         with open(self.pic_log_path, 'a',encoding='utf-8') as f:
        #             f.write(
        #                 "receive pic-->[{time}]:{other_name}({other_ip})-->{self_name}({self_ip}):   {content}\n".format(
        #                     time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        #                     other_name=bean.device_name(),
        #                     other_ip=str(addr[0]),
        #                     self_name=self.my_device_id.text(),
        #                     self_ip=self.my_device_ip.text(),
        #                     content=bean.md_5 + "." + bean.file_ext
        #                 ))
        #         shutil.copyfile(os.path.join(self.IMAGE_PATH, bean.md_5 + bean.file_ext),
        #                         os.path.join(self.image_save_path, "{time}_{other_name}_{other_ip}{file_ext}".format(
        #                             time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        #                             other_name=bean.device_name(),
        #                             other_ip=str(addr[0]),
        #                             file_ext=bean.file_ext
        #                         )))
        #         self.listWidget.addImageMsg(self.MainForm.device_name,
        #                                     os.path.join(self.IMAGE_PATH, bean.md_5 + bean.file_ext), True,
        #                                     ip=str(addr[0]))
        #         self.MainForm.not_read_msg_count_signal.emit()
        #         pic_success_receive_bean = PicSuccessReceiveBean()
        #         pic_success_receive_bean.send(self.MainForm.apply, addr)
        #         self.pic_data_dict.clear()
        #     else:
        #         print("删除")
        #         os.remove(os.path.join(self.IMAGE_PATH, bean.md_5 + bean.file_ext))
