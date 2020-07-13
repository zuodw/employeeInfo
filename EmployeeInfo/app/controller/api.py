import json
import random
import string

from flask import request, session
from flask_mail import Message

from app import app
from app import mail
from app.models.models import Employee
from app.models.models import dbSession


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
    msg = Message('验证码', sender='zuodw@qq.com', recipients=[userMail])
    verifyCode = "".join(random.sample([x for x in string.ascii_letters + string.digits], 6))
    print(verifyCode)
    msg.body = '您的验证码是：' + verifyCode
    mail.send(msg)

    session['mail'] = userMail
    session['verifyCode'] = verifyCode

    return 'ok'


@app.route('/api/SignUp', methods=['POST'])
def SignUp():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']['mail']
    verifyCode = data['params']['verifyCode']
    print(session)
    print(session.get('verifyCode'))
    if userMail == session.get('mail') and verifyCode == session.get('verifyCode'):
        employee = Employee()
        employee.mail = userMail
        dbSession.add(employee)
        dbSession.commit()

    return 'ok'
