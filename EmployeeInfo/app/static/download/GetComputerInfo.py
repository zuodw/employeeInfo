import wmi
import os
import json

w = wmi.WMI()

info = {}


def getComputerInfo():
    info['ComputerInfo'] = {}
    info['ComputerInfo']['memory'] = []
    info['ComputerInfo']['disk'] = []

    for processor in w.Win32_Processor():
        # CPU型号
        info['ComputerInfo']['cpu'] = processor.Name.strip()

    for memModule in w.Win32_PhysicalMemory():
        totalMemSize = int(memModule.Capacity)

        info['ComputerInfo']['memory'].append({
            'fact': memModule.Manufacturer,  # 内存厂商
            'num': memModule.PartNumber.strip(),  # 内存型号
            'size': totalMemSize / 1024 ** 3  # 内存大小
        })

    for disk in w.Win32_DiskDrive(InterfaceType="IDE"):
        diskSize = int(disk.size)

        info['ComputerInfo']['disk'].append({
            'caption': disk.Caption,  # 硬盘名称
            'size': (diskSize / 1024 ** 3)  # 硬盘大小
        })

    for address in w.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        # IP地址
        if '192.168.0.' in address.IPAddress[0]:
            info['ComputerInfo']['ip'] = {}
            info['ComputerInfo']['ip']['ip4'] = address.IPAddress[0]
            info['ComputerInfo']['ip']['ip6'] = address.IPAddress[1]

        # MAC地址
        info['ComputerInfo']['mac'] = address.MACAddress


def main():
    path = os.path.join(os.getcwd(), '_pcinfo.json')

    getComputerInfo()

    # 写入文件信息
    with open(path, 'w+') as fp:
        fp.write(json.dumps(info, indent=4))

    print(path)


if __name__ == '__main__':
    main()
