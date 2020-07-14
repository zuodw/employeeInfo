import json
import random
import string

from flask import request
from flask_mail import Message

from app import app
from app import mail
from app.models.models import Employee
from app.models.models import VerifyInfo
from app.models.models import dbSession

from app.controller.employeecontroller import EmployeeController
from app.controller.verifycontroller import VerifyController


# 发送验证码邮件
def sendVerifyCodeMail(userMail):
    msg = Message('验证码', sender='zuodw@qq.com', recipients=[userMail])
    verifyCode = "".join(random.sample([x for x in string.ascii_letters + string.digits], 6))
    print(verifyCode)
    msg.body = '您的验证码是：' + verifyCode
    mail.send(msg)

    # 认证信息保存
    VerifyController.add(userMail, verifyCode)


@app.route('/api/GetAllEmployeeInfo')
def GetAllEmployeeInfo():
    employees = dbSession.query(Employee).filter(Employee.id == 2).one()
    print(employees)
    return employees.name


@app.route('/api/AddEmployeeInfo', methods=['POST'])
def AddEmployeeInfo():
    employee = Employee()
    data = json.loads(request.get_data(as_text=True))
    employee.name = data['params']['name']
    employee.sex = data['params']['sex']
    employee.idCard = data['params']['idCard']
    employee.birthday = '19901212'
    employee.nation = data['params']['nation']
    employee.nativePlace = data['params']['nativePlace']
    employee.education = data['params']['education']
    employee.school = data['params']['school']
    employee.speciality = data['params']['speciality']
    employee.department = 'web'
    employee.phoneNum = data['params']['phoneNum']
    employee.mail = data['params']['mail']

    dbSession.add(employee)
    dbSession.commit()
    return 'ok'


@app.route('/api/ApplyVerifyCode', methods=['POST'])
def ApplyVerifyCode():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']

    employee = EmployeeController.query_byMail(userMail)

    if employee:
        print("该邮件已经注册!")
        return "该邮件已经注册!"
    else:
        sendVerifyCodeMail(userMail)

    return 'ok'


@app.route('/api/SignUp', methods=['POST'])
def SignUp():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']['mail']
    verifyCode = data['params']['verifyCode']

    vi = VerifyController.query_byMail(userMail)
    if vi:
        if userMail == vi.mail and verifyCode == vi.verifyCode:
            print("Verify Success.")

            # 认证成功，添加用户
            EmployeeController.add(userMail)

            # 删除认证信息
            VerifyController.delete(userMail)
    return 'ok'
