import functools
import struct

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import threads
from mylogging import logger


class UDPProtocol(DatagramProtocol):

    def __init__(self, *, MainForm):
        super(UDPProtocol, self).__init__()
        self.MainForm = MainForm

    def startProtocol(self):
        logger.info("启动udp")

    def datagramReceived(self, datagram, addr):
        # print(datagram)
        # 取出前16个字节，拿到元祖第一个内容，解码utf-8,去除空格

        usage = struct.unpack("!16s", datagram[0:16])[0].decode('utf-8').strip('\x00')
        try:
            function_ = functools.partial(getattr(self, usage + "_handle"), datagram, addr)
            d = threads.deferToThread(function_)
            d.addErrback(lambda m: print(m))

        except AttributeError as e:
            logger.error(e)

    def apply_position_handle(self, datagram, addr):
        '''
        对方请求自己的位置数据
        :param datagram:
        :param addr:
        :return:
        '''
        self.MainForm.apply_position_data_signal.emit(addr)

    def apply_measure_handle(self, datagram, addr):
        '''
        对方请求自己的测量数据
        :param datagram:
        :param addr:
        :return:
        '''
        self.MainForm.apply_measure_data_signal.emit(addr)

    def clear_device_handle(self, datagram, addr):
        '''
        发送而来的清理参数命令
        :param datagram:
        :param addr:
        :return:
        '''
        self.MainForm.clear_device_signal.emit(addr)

    def clear_success_handle(self, datagram, addr):
        self.MainForm.clear_success_signal.emit()

    def net_success_handle(self, datagram, addr):
        # 入网成功
        self.MainForm.reply_for_net_success.emit(datagram)

    def net_failed_handle(self, datagram, addr):
        # 入网失败
        # reply_for_net_failure_obj = ReplyForNetFailureBean.unpack_data(datagram)
        self.MainForm.reply_for_net_failure.emit()

    def position_data_handle(self, datagram, addr):
        '''
        收到位置数据
        :param datagram:
        :param addr:
        :return:
        '''
        self.MainForm.not_read_msg_count_signal.emit()
        self.MainForm.position_data_signal.emit(datagram, addr)

    def measure_data_handle(self, datagram, addr):
        '''
        收到测量数据
        :param datagram:
        :param addr:
        :return:
        '''
        self.MainForm.not_read_msg_count_signal.emit()
        self.MainForm.measure_data_signal.emit(datagram, addr)

    def position_recv_handle(self, datagram, addr):

        self.MainForm.position_recv_signal.emit()

    def measure_recv_handle(self, datagram, addr):
        self.MainForm.measure_recv_signal.emit()

    def connectionRefused(self):
        self.MainForm.connect_refused.emit()

    def send_apply(self, order, addr):
        logger.info(order)
        self.transport.write(order, addr)


if __name__ == '__main__':
    from twisted.internet import reactor
