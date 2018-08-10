'''
请求通话命令
'''
import struct
import struct
import os
import sys

sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property
from trans_data import encode_, decode_


class ApplyForVoiceBean(object):
    __slots__ = ['_usage', '_device_category', '_device_id']
    usage = typed_property('usage', str)
    device_category = typed_property('device_category', str)
    device_id = typed_property('device_id', int)
    typecode = '<16s16si'

    def __init__(self, *, usage='apply_voice', device_category, device_id):
        self.usage = usage
        self.device_category = device_category
        self.device_id = device_id

    def __iter__(self):
        return (i for i in (self.usage,
                            self.device_category,
                            self.device_id))

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self, typecode=typecode):
        bytes_data = [encode_(m) for m in self]
        return struct.pack(typecode, *bytes_data)

    @property
    def device_name(self):
        return self.device_category.split(".")[-1] + "_" + str(self.device_id)

    @property
    def ziwang_name(self):
        return self.device_category.split('.')[-2]

    @classmethod
    def frombytes(cls, bytes_data):
        memv = memoryview(bytes_data)
        data_para = [decode_(x) for x in struct.unpack(cls.typecode, memv[:].tobytes())]
        print(data_para)
        return cls(device_category=data_para[1], device_id=data_para[2])

    def send(self, __send, addr):
        try:
            __send.send_apply(bytes(self), addr)
        except Exception as e:
            print(e)
