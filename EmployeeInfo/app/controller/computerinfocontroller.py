from app.models.models import ComputerInfo
from app.models import dbSession


class ComputerInfoController:
    @staticmethod
    def add(pcNum, cpu, memory, disk, ip, mac):
        computer = ComputerInfo()
        computer.pcNum = pcNum
        computer.cpu = cpu
        computer.memory = memory
        computer.disk = disk
        computer.ip = ip
        computer.mac = mac

        dbSession.add(computer)
        dbSession.commit()
