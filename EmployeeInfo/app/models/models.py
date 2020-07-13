import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from app.models import engine
from app import app
from app.models import dbSession

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    # 邮箱地址
    mail = sa.Column(sa.String(20), primary_key=True)

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

    # 生日(TBD：根据身份证号自动生成)
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
    pcNum = sa.Column(sa.String(20), nullable=True)

    # 备注
    comments = sa.Column(sa.String(500), nullable=True)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
