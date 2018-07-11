import os

# Return CPU temperature as a character string
import reprlib
import time


def getVoiceCardStatus():
    return "Generalplus Technology Inc." in os.popen("lsusb").read()


def getEthernetAdapterStatus():
    return "Fast Ethernet Adapter" in os.popen("lsusb").read()

def getSystemInfo():
    return os.popen('uname -m -r -s').readline()


def getCPUtemperature():
    try:
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            cpu_temp = f.read()
    except:
        cpu_temp = 0
    return "{:.2f}℃".format(float(cpu_temp) / 1000.0)


# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM

def getRAMinfo(type):
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            result = dict(zip(("total","used","free"),tuple(line.split()[1:4])))
            print(result.get(type))
            return "{:.1f}Mb".format(float(result.get(type)) / 1000.0)

# Return % of CPU used by user as a character string
def getCPUuse():
    time1 = os.popen('cat /proc/stat').readline().split()[1:5]
    time.sleep(0.2)
    time2 = os.popen('cat /proc/stat').readline().split()[1:5]
    deltaUsed = int(time2[0]) - int(time1[0]) + int(time2[2]) - int(time1[2])
    deltaTotal = deltaUsed + int(time2[3]) - int(time1[3])
    cpuUsage = float(deltaUsed) / float(deltaTotal) * 100
    # print('CPU Usage is now %.1f' % cpuUsage + '%')

    return "{:.1f}%".format(cpuUsage)


# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def getDiskSpace(type):
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            result = dict(zip(
                ("total","used",'remain',"percentage"),
                tuple(line.split()[1:5])
            ))
            return result.get(type)


# CPU informatiom
# CPU_temp = getCPUtemperature()
# CPU_usage = getCPUuse()
#
# RAM information
# Output is in kb, here I convert it in Mb for readability
# RAM_stats = getRAMinfo(1)
# RAM_total = round(int(RAM_stats[0]) / 1000, 1)
# RAM_used = round(int(RAM_stats[1]) / 1000, 1)
# RAM_free = round(int(RAM_stats[2]) / 1000, 1)
#
# Disk information
# DISK_stats = getDiskSpace()
# DISK_total = DISK_stats[0]
# DISK_used = DISK_stats[1]
# DISK_perc = DISK_stats[3]

if __name__ == '__main__':
    # print('')
    # print('CPU Temperature = ' + str(CPU_temp))
    # print('CPU Use = ' + str(CPU_usage) + "%")
    # print('')
    # print('RAM Total = ' + str(RAM_total) + ' MB')
    # print('RAM Used = ' + str(RAM_used) + ' MB')
    # print('RAM Free = ' + str(RAM_free) + ' MB')
    # print('')
    # print('DISK Total Space = ' + str(DISK_total) + 'B')
    # print('DISK Used Space = ' + str(DISK_used) + 'B')
    # print('DISK Used Percentage = ' + str(DISK_perc))
    # print("Generalplus Technology Inc." in os.popen("lsusb").read())
    pass
    # print(os.popen('uname -a').readline())