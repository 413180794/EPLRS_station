'''
请求通话的回应，允许通话应答
ss
'''
import struct
import os
import sys

sys.path.append(os.path.abspath("../tool"))
from typeProperty import typed_property
from trans_data import encode_


class AcceptVoiceReplyBean(object):
    __slots__ = ['_usage']
    usage = typed_property('usage', str)
    typecode = "<16s"

    def __init__(self):
        self.usage = 'accept_voice_r'

    def __iter__(self):
        return (i for i in (self.usage,))

    def __bytes__(self, typecode=typecode):
        bytes_data = [encode_(m) for m in self]
        return struct.pack(typecode, *bytes_data)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}'.format(class_name)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    @classmethod
    def frombytes(cls):
        return cls()

    def send(self, __send, addr):
        __send.send_apply(bytes(self), addr)


if __name__ == '__main__':
    x = AcceptVoiceReplyBean()
    print(AcceptVoiceReplyBean.frombytes())
    print(bytes(x))
