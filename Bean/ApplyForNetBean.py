import struct
import os
import sys

sys.path.append(os.path.abspath("../tool"))

from typeProperty import typed_property
from trans_data import decode_, encode_


class ApplyForNetBean:
    __slots__ = ['_usage', '_device_category', '_width_band', '_interval',
                 '_routing_parameter', "_device_id"]
    usage = typed_property("usage", str)
    device_category = typed_property("device_category", str)
    width_band = typed_property("width_band", int)
    interval = typed_property("interval", int)
    routing_parameter = typed_property("routing_parameter", str)
    device_id = typed_property("device_id", int)
    typecode = "<16s16sii16si"

    def __init__(self, *, usage='apply_net', device_category, width_band, interval, routing_parameter, device_id):
        self.usage = usage

        self.device_category = device_category
        self.device_id = device_id
        self.width_band = width_band
        self.interval = interval
        self.routing_parameter = routing_parameter

    def __iter__(self):
        return (
            i for i in (self.usage,
                        self.device_category,
                        self.width_band,
                        self.interval,
                        self.routing_parameter,
                        self.device_id
                        )
        )

    def __repr__(self):
        classs_name = type(self).__name__
        return "{}(usage={!r},device_category={!r},width_band={!r},interval={!r},routing_parameter={!r},device_id={!r})".format(
            classs_name, *self)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

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
        return cls(device_category=data_para[1], width_band=data_para[2], interval=data_para[3],
                   routing_parameter=data_para[4],
                   device_id=data_para[5])

    def send(self, __send, addr):
        __send.send_apply(bytes(self), addr)

    def __bool__(self):
        if self.width_band in [437,] and self.interval in [25, 625] and self.routing_parameter in ["OSPF协议", ]:
            return True
        else:
            return False


if __name__ == '__main__':
    x = ApplyForNetBean(device_category='asd', width_band=123, interval=123, routing_parameter='123', device_id=12)
    # print(repr(x))
    # print(eval(repr(x)))
    # print(bytes(x))
    print(ApplyForNetBean.frombytes(bytes(x)))
    # print(bytes(2))
