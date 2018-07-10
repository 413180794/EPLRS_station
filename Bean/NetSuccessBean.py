import struct
# 11
import os
import sys


sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property
from trans_data import encode_, decode_


class NetSuccessBean(object):
    __slots__ = ['_usage', '_ip_list']
    usage = typed_property("usage", str)
    ip_list = typed_property("ip_list", str)
    typecode = '<16s1024s'

    def __init__(self, *, ip_list):
        self.usage = "net_success"
        self.ip_list = ip_list

    def __iter__(self):
        return (i for i in (self.usage, self.ip_list))

    def __bytes__(self,typecode=typecode):
        bytes_data = [encode_(m) for m in self]
        return struct.pack(typecode,*bytes_data)

    @classmethod
    def frombytes(cls,bytes_data):
        memv = memoryview(bytes_data)
        bytes_data = [decode_(x) for x in struct.unpack(cls.typecode,memv[:].tobytes())]
        return cls(ip_list=bytes_data[1])
    def send(self, _send, addr):
        '''
        使用send 向 addr发送数据
        :param send: protocal
        :param addr: 地址
        :return:
        '''
        _send.send_apply(bytes(self), addr)
