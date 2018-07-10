from functools import singledispatch

ENCODE_TYPE = 'utf-8'


@singledispatch
def encode_(obj):
    return obj


@encode_.register(str)
def _(text):
    return text.encode(ENCODE_TYPE)


@encode_.register(int)
def _(n):
    return n


@singledispatch
def decode_(obj):
    return obj


@decode_.register(bytes)
def _(bytes_):
    return bytes_.decode(ENCODE_TYPE).strip("\00")


@decode_.register(int)
def _(n):
    return n
