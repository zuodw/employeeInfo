import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.models import engine
from app import app
from app.models import dbSession

Base = declarative_base()


class ComputerInfo(Base):
    __tablename__ = 'computer'

    # MAC地址(主键)
    MACAddress = sa.Column(sa.String(20), primary_key=True, nullable=True)

    # 电脑厂商
    ComputerSystemManufacturer = sa.Column(sa.String(100), nullable=True)

    # 电脑型号
    ComputerSystemModel = sa.Column(sa.String(100), nullable=True)

    # 电脑系统
    OperatingSystemCaption = sa.Column(sa.String(100), nullable=True)

    # 处理器(CPU)名
    ProcessorSystemName = sa.Column(sa.String(100), nullable=True)

    # 系统名(例:PC108)
    ProcessorName = sa.Column(sa.String(100), nullable=True)

    # 内存厂商01
    PhysicalMemoryManufacturer01 = sa.Column(sa.String(100), nullable=True)

    # 内存型号01
    PhysicalMemoryPartNumber01 = sa.Column(sa.String(100), nullable=True)

    # 内存大小01
    PhysicalMemoryCapacity01 = sa.Column(sa.String(10), nullable=True)

    # 内存厂商02
    PhysicalMemoryManufacturer02 = sa.Column(sa.String(100), nullable=True)

    # 内存型号02
    PhysicalMemoryPartNumber02 = sa.Column(sa.String(100), nullable=True)

    # 内存大小02
    PhysicalMemoryCapacity02 = sa.Column(sa.String(10), nullable=True)

    # 内存厂商03
    PhysicalMemoryManufacturer03 = sa.Column(sa.String(100), nullable=True)

    # 内存型号03
    PhysicalMemoryPartNumber03 = sa.Column(sa.String(100), nullable=True)

    # 内存大小03
    PhysicalMemoryCapacity03 = sa.Column(sa.String(10), nullable=True)

    # 内存厂商04
    PhysicalMemoryManufacturer04 = sa.Column(sa.String(100), nullable=True)

    # 内存型号04
    PhysicalMemoryPartNumber04 = sa.Column(sa.String(100), nullable=True)

    # 内存大小04
    PhysicalMemoryCapacity04 = sa.Column(sa.String(10), nullable=True)

    # 硬盘名称01
    DiskDriveCaption01 = sa.Column(sa.String(100), nullable=True)

    # 硬盘大小01
    DiskDriveSize01 = sa.Column(sa.String(10), nullable=True)

    # 硬盘名称02
    DiskDriveCaption02 = sa.Column(sa.String(100), nullable=True)

    # 硬盘大小02
    DiskDriveSize02 = sa.Column(sa.String(10), nullable=True)

    # 硬盘名称03
    DiskDriveCaption03 = sa.Column(sa.String(100), nullable=True)

    # 硬盘大小03
    DiskDriveSize03 = sa.Column(sa.String(10), nullable=True)

    # 硬盘名称04
    DiskDriveCaption04 = sa.Column(sa.String(100), nullable=True)

    # 硬盘大小04
    DiskDriveSize04 = sa.Column(sa.String(10), nullable=True)

    # ipv4地址
    IPv4Address = sa.Column(sa.String(20), nullable=True)

    # ipv6地址
    IPv6Address = sa.Column(sa.String(30), nullable=True)


class Employee(Base):
    __tablename__ = 'employee'

    # 主键
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)

    # 邮箱地址
    mail = sa.Column(sa.String(50), nullable=False)

    # 密码
    password = sa.Column(sa.String(50), nullable=False)

    # 姓名
    name = sa.Column(sa.String(20), nullable=True)

    # 性别
    sex = sa.Column(sa.String(20), nullable=True)

    # 民族
    nation = sa.Column(sa.String(20), nullable=True)

    # 籍贯
    nativePlace = sa.Column(sa.String(50), nullable=True)

    # 身份证号
    idCard = sa.Column(sa.String(30), nullable=True)

    # 护照ID(可以为空)
    passportId = sa.Column(sa.String(20), nullable=True)

    # 生日(根据身份证号自动生成)
    birthday = sa.Column(sa.Date, nullable=True)

    # 入职时间(默认为填写日期)
    entryTime = sa.Column(sa.Date, nullable=True)

    # 学历
    education = sa.Column(sa.String(20), nullable=True)

    # 毕业院校
    school = sa.Column(sa.String(20), nullable=True)

    # 专业
    speciality = sa.Column(sa.String(80), nullable=True)

    # 部门
    department = sa.Column(sa.String(20), nullable=True)

    # 职务
    duty = sa.Column(sa.String(20), nullable=True)

    # 联系电话
    phoneNum = sa.Column(sa.String(20), nullable=True)

    # 门禁卡编号
    accessCard = sa.Column(sa.String(20), nullable=True)

    # 电脑编号
    MACAddress = sa.Column(sa.String(20), ForeignKey('computer.MACAddress'))
    computer = relationship("ComputerInfo", backref="computer_of_employee")

    # 备注
    comments = sa.Column(sa.String(500), nullable=True)


class VerifyInfo(Base):
    __tablename__ = 'verifyinfo'

    # 主键
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)

    # mail
    mail = sa.Column(sa.String(50), primary_key=True)

    # verifyCode
    verifyCode = sa.Column(sa.String(20), nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
