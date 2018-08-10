import struct
import os
import sys

sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property

from trans_data import encode_, decode_


class PositionDataBean:
    __slots__ = ['_usage', '_device_category', '_device_id', '_position_x', '_position_y', '_position_z']
    usage = typed_property("usage", str)
    device_category = typed_property("device_category", str)
    device_id = typed_property("device_id", int)
    position_x = typed_property("position_x", float)
    position_y = typed_property("position_y", float)
    position_z = typed_property("position_z", float)
    typecode = '<16s16siddd'

    def __init__(self, *, usage='position_data', device_category, device_id, position_x, position_y, position_z):
        self.usage = usage
        self.device_category = device_category
        self.device_id = device_id
        self.position_x = float(position_x)
        self.position_y = float(position_y)
        self.position_z = float(position_z)

    def __iter__(self):
        return (i for i in
                (self.usage, self.device_category, self.device_id, self.position_x, self.position_y, self.position_z))

    def device_kind(self):
        return "模拟电台" if self.device_category.split("_")[-1] == "r" else "虚拟电台"

    @property
    def device_name(self):
        return self.device_category.split(".")[-1] + "_" + str(self.device_id)

    @property
    def ziwang_name(self):
        return self.device_category.split('.')[-2]

    def __bytes__(self, typecode=typecode):
        bytes_data = [encode_(m) for m in self]
        return struct.pack(typecode, *bytes_data)

    @classmethod
    def frombytes(cls, bytes_data):
        memv = memoryview(bytes_data)
        data_para = [decode_(x) for x in struct.unpack(cls.typecode, memv[:].tobytes())]
        return cls(device_category=data_para[1], device_id=data_para[2], position_x=data_para[3],
                   position_y=data_para[4], position_z=data_para[5])

    def send(self, _send, addr):
        '''
        使用send 向 addr发送数据
        :param send: protocal
        :param addr: 地址
        :return:
        '''
        _send.send_apply(bytes(self), addr)

    def __str__(self):
        return "经度:{:.3f}°,纬度:{:.3f}°,高度:{:.3f}km".format(self.position_x, self.position_y, self.position_z)


if __name__ == '__main__':
    x = PositionDataBean(device_category="mse_t_v", device_id=12, position_x=12, position_y=23, position_z=12)
    print(x)
