from app.models.models import Employee
from app.models import DBSession
from app.models.models import session
from app.models.models import Base
from app.models import engine

Base.metadata.create_all(engine)

# 增加数据
employee = Employee()
employee.name = '战神'
employee.sex = '男'
employee.nation = '汉族'
employee.nativePlace = '山东青岛'
employee.idCard = '111111111111111111'
employee.birthday = '20200202'
employee.passportId = ''
employee.entryTime = '20200202'
employee.education = '本科'
employee.school = '家里蹲大学'
employee.speciality = '修理地球专业'
employee.department = '开发'
employee.duty = '监事'
employee.phoneNum = '18888888888'
employee.mail = 'zzz@163.com'
employee.accessCard = ''
employee.pcNum = ''
employee.comments = ''


session.add(employee)
session.commit()
session.close()


