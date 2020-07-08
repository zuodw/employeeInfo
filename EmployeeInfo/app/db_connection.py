from app.models.models import Employee
from app.models import DBSession
from app.models.models import session
from app.models.models import Base
from app.models import engine

Base.metadata.create_all(engine)

# 增加数据
employee = Employee()
employee.name = '左大伟'
employee.sex = '男'
employee.idCard = '370285198904125610'
employee.passportId = ''
employee.birthday = '19890412'
employee.nation = '汉族'
employee.entryTime = '20180402'
employee.education = '本科'
employee.school = '太原理工大学'
employee.speciality = '数学与应用数学'
employee.department = '嵌入式开发组'
employee.duty = '监事'
employee.phoneNum = '18624421163'
employee.accessCard = ''
employee.pcNum = ''
employee.comments = ''


session.add(employee)
session.commit()
session.close()


