import struct
import os
import sys



sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property
from trans_data import encode_, decode_

class VoiceDataBean(object):
    __slots__ = ['_usage', '_device_category', '_device_id', '_voice_data']

    usage = typed_property('usage', str)
    device_category = typed_property('device_category', str)
    device_id = typed_property('device_id', int)
    voice_data = typed_property('voice_data', bytes)
    typecode = '<16s16si360s'
    typecode_without_voice = "<16s16si"

    def __init__(self, *, device_category, device_id, voice_data):
        self.usage = 'voice_data'
        self.device_category = device_category
        self.device_id = device_id
        # 待解决问题。如果获得voice_data,
        # 不在bean中解决，bean中数据不具有特殊型
        self.voice_data = voice_data

    def __iter__(self):
        return (i for i in (self.usage, self.device_category, self.device_id, self.voice_data))

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
        data_para = [decode_(x) for x in struct.unpack(cls.typecode_without_voice, memv[:36].tobytes())]
        return cls(device_category=data_para[1], device_id=data_para[2], voice_data=memv[36:].tobytes())

    def send(self, _send, addr):
        _send.send_apply(bytes(self), addr)
