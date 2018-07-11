import struct
import os
import sys



sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property
from trans_data import encode_

class ClearDeviceBean(object):
    __slots__ = ['_usage']
    usage = typed_property('usage', str)
    typecode = '<16s'

    def __init__(self):
        self.usage = 'clear_device'

    def __iter__(self):
        return (i for i in (self.usage,))

    def __bytes__(self, typecode=typecode):
        bytes_data = [encode_(m) for m in self]
        return struct.pack(typecode, *bytes_data)

    @classmethod
    def frombytes(cls):
        return cls()

    def send(self, _send, addr):
        _send.send_apply(bytes(self), addr)