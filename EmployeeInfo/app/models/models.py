import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from app.models import engine
from app import app
from app.models import session

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    # 主键
    id = sa.Column(sa.Integer, primary_key=True)

    # 姓名
    name = sa.Column(sa.String(20), nullable=False)

    # 性别
    sex = sa.Column(sa.String(20), nullable=False)

    # 身份证号
    idCard = sa.Column(sa.String(30), nullable=False)

    # 护照ID(可以为空)
    passportId = sa.Column(sa.String(20), nullable=True)

    # 年龄(TBD：根据身份证号自动生成)
    birthday = sa.Column(sa.Date, nullable=False)

    # 民族
    nation = sa.Column(sa.String(20), nullable=False)

    # 入职时间
    entryTime = sa.Column(sa.Date, nullable=True)

    # 学历
    education = sa.Column(sa.String(20), nullable=False)

    # 毕业院校
    school = sa.Column(sa.String(20), nullable=False)

    # 专业
    speciality = sa.Column(sa.String(80), nullable=False)

    # 部门
    department = sa.Column(sa.String(20), nullable=False)

    # 职务
    duty = sa.Column(sa.String(20), nullable=True)

    # 联系电话
    phoneNum = sa.Column(sa.String(20), nullable=False)

    # 门禁卡编号
    accessCard = sa.Column(sa.String(20), nullable=True)

    # 电脑编号
    pcNum = sa.Column(sa.String(20), nullable=True)

    # 备注
    comments = sa.Column(sa.String(500), nullable=True)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
