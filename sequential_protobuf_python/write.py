import metric_pb2

my_metric = metric_pb2.Metric()
my_metric.name = 'sys.cpu'
my_metric.type = 'gauge'
my_metric.value = 99.9
my_metric.tags.extend(['my_tag', 'foo:bar'])

print(my_metric)
# WRITE
with open('out.bin', 'wb') as f:
    f.write(my_metric.SerializeToString())


# READ
read_metric = None
with open('out.bin', 'rb') as f:
    read_metric = metric_pb2.Metric()
    read_metric.ParseFromString(f.read())
    
print(read_metric)
