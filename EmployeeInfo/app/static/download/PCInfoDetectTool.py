import wmi
import os
import json
from urllib import request, response
import tkinter.messagebox
from tkinter import *


w = wmi.WMI()

info = {
    'ComputerSystem': {
        'Manufacturer': '',
        'Model': ''
    },
    'OperatingSystem': {
        'Caption': ''
    },
    'Processor':
    {
        'SystemName': '',
        'Name': ''
    },
    'PhysicalMemory': [],
    'DiskDrive': [],
    'IPAddress': {
        'IPv4': '',
        'IPv6': ''
    },
    'MACAddress': ''
}


def getComputerInfo():
    # 机器信息
    ComputerSystem = w.Win32_ComputerSystem()[0]
    info['ComputerSystem']['Manufacturer'] = ComputerSystem.Manufacturer
    info['ComputerSystem']['Model'] = ComputerSystem.Model

    # 系统信息
    OperatingSystem = w.Win32_OperatingSystem()[0]
    info['OperatingSystem']['Caption'] = OperatingSystem.Caption

    # CPU
    Processor = w.Win32_Processor()[0]
    info['Processor']['SystemName'] = Processor.SystemName.strip()   # 系统名
    info['Processor']['Name'] = Processor.Name.strip()   # CPU型号

    # 内存
    for PhysicalMemory in w.Win32_PhysicalMemory():
        info['PhysicalMemory'].append({
            'Manufacturer': PhysicalMemory.Manufacturer,                # 内存厂商
            'PartNumber': PhysicalMemory.PartNumber.strip(),            # 内存型号
            'Capacity': int(PhysicalMemory.Capacity) / (1024 ** 3)      # 内存大小
        })

    # 硬盘
    for diskDrive in w.Win32_DiskDrive():
        info['DiskDrive'].append({
            'Caption': diskDrive.Caption,                       # 硬盘名称
            'Size': round(int(diskDrive.size) / (1024 ** 3))    # 硬盘大小
        })

    for address in w.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        # IP地址
        if '192.168.0.' in address.IPAddress[0]:
            info['IPAddress'] = {}
            info['IPAddress']['IPv4'] = address.IPAddress[0]
            info['IPAddress']['IPv6'] = address.IPAddress[1]

        # MAC地址
        info['MACAddress'] = address.MACAddress

    print(info)


def sendComputerInfoToServer():
    # 隐藏主界面
    tkinter.Tk().withdraw();

    req = request.Request(url='http://192.168.0.102:5000/api/SetComputerInfo')
    try:
        response = request.urlopen(req, bytes(json.dumps(info), 'utf8')).read()
    except Exception as e:
        tkinter.messagebox.showinfo("糟糕", 'PC信息上传失败！')
        return

    data = json.loads(str(response, 'utf8'))
    if data['errCode'] == '0':
        tkinter.messagebox.showinfo("恭喜", 'PC信息上传成功！')
    else:
        tkinter.messagebox.showinfo("糟糕", 'PC信息上传失败！')


def main():
    # PC信息取得
    getComputerInfo()

    # 发送PC信息至服务器
    sendComputerInfoToServer()


if __name__ == '__main__':
    main()
