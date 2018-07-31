import os
import sys
import time
from queue import Queue
from pexpect import spawn
unit_ = ['B', 'KB', 'MB', 'GB', 'TB']

password = 'ubuntu'
def control_net_speed(interface, speed):
    command_del = 'sudo tc qdisc del dev {} root'.format(interface)
    command = 'sudo tc qdisc add dev {} root tbf rate {} burst 2048kbit latency 400ms'.format(interface, speed)
    spawn(command_del).sendline(password)
    spawn(command).sendline(password)


def get_net_data(interface):
    if not os.path.exists('/proc/net/dev'):
        return None
    for line in open('/proc/net/dev', 'r'):
        if line.split(':')[0].find(interface) >= 0:
            return list(map(int, line.split(':')[1].split()))


queue = Queue(1)


def convert_bytes_to_string(b):
    cnt = 0
    while b >= 1024.0:
        b = float(b) / 1024.0
        cnt += 1
    return '%.2f%s' % (b, unit_[cnt])


def get_net_data_num(interface):
    net_data = get_net_data(interface)
    if net_data is None:
        return None
    else:
        return net_data[0]


def get_download_speed(interface):
    '''
    有问题
    :param interface:
    :return:
    '''
    queue.put(get_net_data_num(interface))
    while True:
        net_data_num = get_net_data_num(interface)
        if net_data_num is None:
            yield None
        else:
            if queue.full():
                old_net_data_num = queue.get()
                download_speed = (float(net_data_num) - float(old_net_data_num))
                print(download_speed)
                yield convert_bytes_to_string(download_speed)
                queue.put(net_data_num)


if __name__ == '__main__':
    interface = "enp3s0"
    control_net_speed(interface,'3.84kbit')
    '''
    net_data = get_net_data(interface)
    receive_data_bytes = net_data[0]
    queue.put(receive_data_bytes)
    while True:
        net_data = get_net_data(interface)
        receive_data_bytes = net_data[0]
        print(queue.qsize())
        if queue.full():
            old_re = queue.get()
            download_speed = (float(receive_data_bytes) - float(old_re))
            print(convert_bytes_to_string(download_speed))
            print((float(receive_data_bytes) - float(old_re)) / 1024.0)
            queue.put(receive_data_bytes)

        transmit_data_bytes = net_data[8]
        print('Interface:%s  -> Receive Data: %s  Transmit Data: %s' % (
            interface, convert_bytes_to_string(receive_data_bytes), convert_bytes_to_string(transmit_data_bytes)))
        time.sleep(1)
    '''