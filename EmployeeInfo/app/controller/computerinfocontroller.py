from app.models.models import ComputerInfo
from app.models import dbSession


class ComputerInfoController:
    @staticmethod
    def query_byMac(mac):
        computerInfo = dbSession.query(ComputerInfo).filter(ComputerInfo.MACAddress == mac).first()
        if not computerInfo:
            return None
        else:
            return computerInfo

    @staticmethod
    def query_byIPv4(ipv4):
        computerInfo = dbSession.query(ComputerInfo).filter(ComputerInfo.IPv4Address == ipv4).first()
        if not computerInfo:
            return None
        else:
            return computerInfo
