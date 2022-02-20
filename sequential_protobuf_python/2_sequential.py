import metric_pb2
from random import random

from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32

with open('out.bin', 'wb') as f:
    my_tags = ['my_tag', 'foo:bar']
    for i in range(5):
        my_metric = metric_pb2.Metric()
        my_metric.name = 'sys.cpu'
        my_metric.type = 'gauge'
        my_metric.value = round(random(), 2)
        my_metric.tags.extend(my_tags)

        size = my_metric.ByteSize()
        f.write(_VarintBytes(size))
        f.write(my_metric.SerializeToString())
        print(size, my_metric)

print('====' * 20)

with open('out.bin', 'rb') as f:
    buf = f.read()
    n = 0
    while n < len(buf):
        msg_len, new_pos = _DecodeVarint32(buf, n)
        n = new_pos
        msg_buf = buf[n : n + msg_len]
        n += msg_len
        read_metric = metric_pb2.Metric()
        read_metric.ParseFromString(msg_buf)
        print(msg_len, read_metric)