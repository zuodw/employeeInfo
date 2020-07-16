import json
import random
import string
import os

from flask import request, jsonify, send_from_directory
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
    try:
        mail.send(msg)
    except Exception as e:
        return False

    # 认证信息保存
    VerifyController.add(userMail, verifyCode)
    return True


@app.route('/api/GetAllEmployeeInfo')
def GetAllEmployeeInfo():
    employees = dbSession.query(Employee).filter(Employee.id == 2).one()
    print(employees)
    return employees.name


@app.route('/api/UpdateEmployeeInfo', methods=['POST'])
def UpdateEmployeeInfo():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']['mail']
    employee = EmployeeController.query_byMail(userMail)
    employee.name = data['params']['name']
    employee.sex = data['params']['sex']
    employee.idCard = data['params']['idCard']
    employee.birthday = employee.idCard[6:14]
    employee.nation = data['params']['nation']
    employee.nativePlace = data['params']['nativePlace']
    employee.education = data['params']['education']
    employee.school = data['params']['school']
    employee.speciality = data['params']['speciality']
    employee.department = ''
    employee.phoneNum = data['params']['phoneNum']
    employee.mail = data['params']['mail']

    EmployeeController.update(employee)

    return jsonify({'errCode': '0', 'errMsg': 'OK'})


@app.route('/api/ApplyVerifyCode', methods=['POST'])
def ApplyVerifyCode():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']

    employee = EmployeeController.query_byMail(userMail)

    if employee:
        print("该邮件已经注册!")
        return {'errCode': '-2', 'errMsg': '该邮件已经注册!请直接登录。'}
    else:
        if not sendVerifyCodeMail(userMail):
            return jsonify({'errCode': '-1', 'errMsg': '邮件发送失败'})

    return jsonify({'errCode': '0', 'errMsg': 'OK'})


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

    return jsonify({'errCode': '0', 'errMsg': 'OK'})


@app.route('/api/GetPersonalInfo', methods=['GET'])
def GetPersonalInfo():
    employee = EmployeeController.query_byMail(request.args.to_dict()['mail'])
    return jsonify({
        'errCode': '0',
        'errMsg': 'OK',
        'params': {
            'mail': employee.mail,
            'name': employee.name,
            'birthday': employee.birthday
        }
    })


@app.route('/api/download', methods=['GET', 'POST'])
def Download():
    return send_from_directory(os.path.join(os.getcwd(), "static/download"), filename="GetComputerInfo.py", as_attachment=True)
