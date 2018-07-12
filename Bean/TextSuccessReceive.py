import struct
import os
import sys

from mylogging import logger

sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property
from trans_data import encode_


class TextSuccessReceive(object):
    __slots__ = ['_usage']
    usage = typed_property("usage", str)
    typecode = '<16s'

    def __init__(self):
        self.usage = "text_received"

    def __iter__(self):
        return (i for i in (self.usage,))

    def __bytes__(self):
        bytes_data = [encode_(m) for m in self]
        return struct.pack(self.typecode, *bytes_data)

    @classmethod
    def frombytes(cls):
        return cls()

    def send(self, _send, addr):
        _send.send_apply(bytes(self), addr)


if __name__ == '__main__':
    x = TextSuccessReceive()
    print(bytes(x))
