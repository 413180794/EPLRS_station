import struct
import os
import sys
from datetime import datetime

from mylogging import logger

sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property
from trans_data import encode_, decode_


class TextDataBean(object):
    __slots__ = ['_usage', '_device_category', '_device_id', '_data']
    usage = typed_property("usage", str)
    device_category = typed_property("device_category", str)
    device_id = typed_property("device_id", int)
    data = typed_property("data", str)
    typecode = '<16s16si1024s'

    def __init__(self, *, device_category, device_id, data):
        self.usage = "text_data"
        self.device_category = device_category
        self.device_id = device_id
        self.data = data

    def __iter__(self):
        return (i for i in (self.usage,
                            self.device_category,
                            self.device_id,
                            self.data))

    @property
    def device_name(self):
        return self.device_category + "_" + str(self.device_id)

    def __bytes__(self, typecode=typecode):
        bytes_data = [encode_(m) for m in self]
        return struct.pack(typecode, *bytes_data)

    @classmethod
    def frombytes(cls, bytes_data):
        memv = memoryview(bytes_data)
        data_para = [decode_(x) for x in struct.unpack(cls.typecode, memv[:].tobytes())]
        return cls(device_category=data_para[1], device_id=data_para[2], data=data_para[3])

    def send(self, _send, addr):
        '''
        使用send 向 addr发送数据
        :param send: protocal
        :param addr: 地址
        :return:
        '''
        try:
            _send.send_apply(bytes(self), addr)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print(123)
