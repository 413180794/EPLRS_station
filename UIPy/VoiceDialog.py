import audioop
import wave
from datetime import datetime
import os

import pyaudio
from PyQt5.QtCore import pyqtSlot, QTimer, pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox
import sys



sys.path.append(os.path.abspath("../Bean"))
from AcceptVoiceReplyBean import AcceptVoiceReplyBean
from ApplyForVoiceBean import ApplyForVoiceBean
from RejectVoiceApplyBean import RejectVoiceApplyBean
from VoiceDataBean import VoiceDataBean
from voiceWindows import Ui_Dialog
import speex
from mylogging import logger

# linux与mac交互测试成功。目前来说还有一些小问题，不应该自己给自己发送语音。要限制这种行为

class VoiceDialog(QDialog, Ui_Dialog):
    reject_voice_r_signal = pyqtSignal()
    reject_voice_a_signal = pyqtSignal()
    accept_voice_r_signal = pyqtSignal(tuple)
    voice_data_signal = pyqtSignal(bytes, tuple)

    def __init__(self, MainForm=None):
        super(VoiceDialog, self).__init__()
        self.setupUi(self)
        self.MainForm = MainForm
        self.on_connecting_flag = False  # 判断是否正在通话中。
        self.reject_voice_r_signal.connect(self.on_reject_voice_r_signal)
        self.reject_voice_a_signal.connect(self.on_reject_voice_a_signal)
        self.accept_voice_r_signal.connect(self.on_accept_voice_r_signal)
        self.voice_data_signal.connect(self.on_voice_data_signal)
        self.audio_save_path = os.path.join("..","saveAudio")
        self.ifanswer = QTimer(self)  # 一次性定时器，判断10秒后正在建立连接状态是否改变，对方有无应答
        self.ifanswer.timeout.connect(self.no_anwser)
        self.ifanswer.setSingleShot(True)
        # self 需要两个定时器，一个用于主动向self.device_ip 发送语音
        # 一个用于被动向self.other_addr 发送语音。
        # 一个主动发送，一个被动发送
        self.ifremove_wav = True
        self.CHUNK = 6400  # 语音一次读取的大小
        self.WIDTH = 1
        self.CHANNELS = 1
        self.RATE = 8000
        self.FORMAT = pyaudio.paInt16

        self.speexEncode = speex.SpeexEncoder(speex.SPEEX_MODEID_UWB)
        self.speexDecode = speex.SpeexDecoder(speex.SPEEX_MODEID_UWB)

        self.input_stream = None
        self.output_stream = pyaudio.PyAudio().open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            output=True,
            frames_per_buffer=self.CHUNK,
        )
        self.send_audio_file_name = None
        self.receive_audio_file_name = None
        self.send_wf = None
        self.receive_wf = None

    def my_callback(self, voice_data, frame_count, time_info, status):
        if voice_data is not None:
            # if self.send_audio_file_name is not None:
            #     with open(self.send_audio_file_name, 'ab') as f:
            #         f.write(voice_data)
            if not os.path.exists(self.send_audio_file_name):
                self.send_wf = wave.open(self.send_audio_file_name, 'wb')
                self.send_wf.setnchannels(self.CHANNELS)
                self.send_wf.setsampwidth(pyaudio.PyAudio().get_sample_size(self.FORMAT))
                self.send_wf.setframerate(self.RATE)
                self.send_wf.writeframes(voice_data)
            else:
                self.send_wf.writeframes(voice_data)
            print('send before compress' + str(len(voice_data)))
            compress_voice_data = self.speexEncode.encode(voice_data)  # 使用speex库进行压缩
            print('send after compress' + str(len(compress_voice_data)))
            # if self.send_audio_file_name is not None:
            #     with open(self.send_audio_file_name, 'ab') as f:
            #         f.write(voice_data)

            device_category, device_id = self.device_name_label.text().rsplit("_", maxsplit=1)
            voice_data_bean = VoiceDataBean(device_category=device_category, device_id=int(device_id),
                                            voice_data=compress_voice_data)

            voice_data_bean.send(self.MainForm.apply, (self.device_ip_label.text(), self.MainForm.MYPORT))
        return (None, pyaudio.paContinue)

    def on_voice_data_signal(self, datagram, addr):
        voice_data_bean = VoiceDataBean.frombytes(datagram)
        # print(voice_data_bean.voice_data)
        print("shoudaoqian" + str(len(voice_data_bean.voice_data)))
        voice_data = self.speexDecode.decode(voice_data_bean.voice_data)  # 解压缩

        if self.receive_audio_file_name is not None:
            if not os.path.exists(self.receive_audio_file_name):
                self.receive_wf = wave.open(self.receive_audio_file_name, 'wb')
                self.receive_wf.setnchannels(self.CHANNELS)
                self.receive_wf.setsampwidth(pyaudio.PyAudio().get_sample_size(self.FORMAT))
                self.receive_wf.setframerate(self.RATE)
                self.receive_wf.writeframes(voice_data)
                with open(self.receive_audio_file_name, 'ab') as f:
                         f.write(voice_data_bean.voice_data)
            else:
                self.receive_wf.writeframes(voice_data)

        # print("shoudaohou" + str(len(voice_data)))
        self.output_stream.write(voice_data)

    def on_reject_voice_r_signal(self):
        '''
        对方拒绝了语音请求，提示对方拒绝语音请求，结束
        :return:
        '''
        if self.status_label.text() == "正在建立连接":
            self.status_label.setText("对方拒绝语音请求")

    def on_reject_voice_a_signal(self):
        '''
        对方挂断了语音
        :return:
        '''
        if self.input_stream is None:
            self.status_label.setText("对方已挂断")
            self.receive_audio_file_name = None
            self.send_audio_file_name = None
            self.receive_wf = None
            self.send_wf = None

        elif self.input_stream.is_active():
            self.input_stream.stop_stream()
            self.status_label.setText("对方已挂断")
            self.receive_audio_file_name = None
            self.send_audio_file_name = None
            self.receive_wf = None
            self.send_wf = None

    def on_accept_voice_r_signal(self, addr):
        '''
        对方允许语音请求，,而且当前处于正在拨号的状态，向对方发送语音,
        对方允许语音请求，那么就要开始向对方发送语音。
        :return:
        '''
        if self.status_label.text() == "正在建立连接":
            self.status_label.setText("正在通话")
            # 得知对方允许通话之后，也需要向对方发送一条允许通话命令
            accept_voice_reply_bean = AcceptVoiceReplyBean()
            accept_voice_reply_bean.send(self.MainForm.apply, addr)
            # self.voice_stream_timer.start()  # 开始发送语音
            if self.input_stream is None:
                self.input_stream = pyaudio.PyAudio().open(
                    format=self.FORMAT,
                    channels=self.CHANNELS,
                    rate=self.RATE,
                    input=True,
                    frames_per_buffer=self.CHUNK,
                    stream_callback=self.my_callback
                )
            self.input_stream.start_stream()
            self.send_audio_file_name = os.path.join(self.audio_save_path,"{time}_send_to_{other_device_name}.wav".format(
                other_device_name=self.device_name_label.text(),
                time=datetime.now().strftime('%Y_%m_%d_%H_%M_%S')))

            self.receive_audio_file_name = os.path.join(self.audio_save_path,"{time}_receive_from_{other_device_name}.wav".format(
                other_device_name=self.device_name_label.text(),
                time=datetime.now().strftime('%Y_%m_%d_%H_%M_%S')))
            print(self.receive_audio_file_name)
    def closeEvent(self, QClosewEvent):
        if self.input_stream is None:
            self.receive_audio_file_name = None
            self.send_audio_file_name = None
            pass
        elif self.input_stream.is_active():
            self.input_stream.stop_stream()
            reject_voice_apply_bean = RejectVoiceApplyBean()
            reject_voice_apply_bean.send(self.MainForm.apply, (self.device_ip_label.text(), self.MainForm.MYPORT))
            self.receive_audio_file_name = None
            self.send_audio_file_name = None

        self.status_label.setText("等待拨号")
        self.device_ip_label.setText("")
        self.device_name_label.setText("")

    @pyqtSlot()
    def on_close_button_clicked(self):
        self.close()

    def no_anwser(self):
        '''
            10秒后如果还是正在建立连接，那么则提示对方没有应答。
        :return:
        '''
        if self.status_label.text() == "正在建立连接":
            self.status_label.setText("对方无应答")
            QMessageBox.critical(self, "对方无应答", "对方无应答")

    @pyqtSlot()
    def on_start_voice_button_clicked(self):
        '''
            点击拨号按钮，向对应的ip发送请求通话命令，取消拨号按钮，只显示挂断按钮
            状态变为正在建立连接，并创建回调，10秒后判断状态是否已经改变，如果没有，状态切换未对方无应答，
        :return:
        '''
        device_category, device_id = self.device_name_label.text().rsplit("_", maxsplit=1)
        # print(device_category)
        # print(device_id)
        bean = ApplyForVoiceBean(
            device_category=device_category,
            device_id=int(device_id),
        )
        bean.send(self.MainForm.apply, (self.device_ip_label.text(), self.MainForm.MYPORT))
        self.close_button.setVisible(True)
        self.start_voice_button.setVisible(False)
        self.status_label.setText("正在建立连接")
        # 10秒后将验证是否有回复，如果有回复，就什么也不做，如果没有回复，提示对方无应答。
        self.ifanswer.start(15000)


if __name__ == '__main__':
    x = "mse_v_r_12"
    m, n = x.rsplit('_', maxsplit=1)
    # mse_v_r
    print(m)
    print(n)
