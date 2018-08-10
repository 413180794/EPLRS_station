import struct
import os
import sys

sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property
from trans_data import encode_, decode_


class MeasureDataBean:
    __slots__ = ['_usage', '_device_category', '_device_id', "_temperature"]
    usage = typed_property("usage", str)
    device_category = typed_property("device_category", str)
    device_id = typed_property("device_id", int)
    temperature = typed_property("temperature", float)
    typecode = '<16s16sid'

    def __init__(self, *, usage="measure_data", device_category, device_id, temperature):
        self.usage = usage
        self.device_category = device_category
        self.device_id = device_id
        self.temperature = temperature

    def __iter__(self):
        return (i for i in (self.usage, self.device_category, self.device_id, self.temperature))

    def device_kind(self):
        return "模拟电台" if self.device_category.split("_")[-1] == "r" else "虚拟电台"

    @property
    def device_name(self):
        return self.device_category.split(".")[-1] + "_" + str(self.device_id)
    @property
    def ziwang_name(self):
        return self.device_category.split(".")[-2]
    def __bytes__(self, typecode=typecode):
        bytes_data = [encode_(m) for m in self]
        return struct.pack(typecode, *bytes_data)

    @classmethod
    def frombytes(cls, bytes_data):
        memv = memoryview(bytes_data)
        bytes_data = [decode_(x) for x in struct.unpack(cls.typecode, memv[:].tobytes())]
        return cls(device_category=bytes_data[1], device_id=bytes_data[2], temperature=bytes_data[3])

    def send(self, _send, addr):
        '''
        使用send 向 addr发送数据
        :param send: protocal
        :param addr: 地址
        :return:
        '''

        _send.send_apply(bytes(self), addr)


    def __str__(self):
        return str(self.temperature)


if __name__ == '__main__':
    x = MeasureDataBean(device_category="123", device_id=123, temperature=123.2)
    print(bytes(x))
