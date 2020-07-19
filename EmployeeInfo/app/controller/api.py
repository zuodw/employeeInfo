import json
import random
import string
import os
import time

from flask import request, jsonify, send_from_directory
from flask_mail import Message
from werkzeug.utils import secure_filename

from app import app
from app import mail
from app.models.models import Employee
from app.models.models import VerifyInfo
from app.models.models import ComputerInfo
from app.models.models import dbSession

from app.controller.employeecontroller import EmployeeController
from app.controller.verifycontroller import VerifyController
from app.controller.computerinfocontroller import ComputerInfoController


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


@app.route('/api/GetEmployeeInfoByMail')
def GetEmployeeInfoByMail():
    employee = EmployeeController.query_byMail(request.args.to_dict()['mail'])
    if not employee:
        return jsonify({'errCode': '-5', 'errMsg': '用户不存在'})

    return jsonify({
        'errCode': '0',
        'errMsg': 'OK',
        'params': {
            'mail': employee.mail,
            'name': employee.name,
            'sex': employee.sex,
            'nation': employee.nation,
            'nativePlace': employee.nativePlace,
            'idCard': employee.idCard,
            'passportId': employee.passportId,
            'education': employee.education,
            'school': employee.school,
            'speciality': employee.speciality,
            'department': employee.department,
            'phoneNum': employee.phoneNum,
            'birthday': employee.birthday
        }
    })


@app.route('/api/UpdateEmployeeInfo', methods=['POST'])
def UpdateEmployeeInfo():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']['mail']
    employee = EmployeeController.query_byMail(userMail)
    employee.name = data['params']['name']
    employee.sex = data['params']['sex']
    employee.idCard = data['params']['idCard']
    if employee.idCard:
        employee.birthday = employee.idCard[6:14]
    else:
        employee.birthday = '19491001'
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
    userMail = data['params']['mail']

    employee = EmployeeController.query_byMail(userMail)

    if employee:
        return {'errCode': '-2', 'errMsg': '该邮件已经注册!请直接登录。'}
    else:
        if not sendVerifyCodeMail(userMail):
            return jsonify({'errCode': '-1', 'errMsg': '邮件发送失败'})

    return jsonify({'errCode': '0', 'errMsg': 'OK'})


@app.route('/api/SignUp', methods=['POST'])
def SignUp():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']['mail']
    password = data['params']['pass']
    verifyCode = data['params']['verifyCode']

    vi = VerifyController.query_byMail(userMail)
    if vi:
        if userMail == vi.mail and verifyCode == vi.verifyCode:
            # 认证成功，添加用户
            EmployeeController.add(userMail, password)

            # 删除认证信息
            VerifyController.delete(userMail)

    return jsonify({'errCode': '0', 'errMsg': 'OK'})


@app.route('/api/SignIn', methods=['POST'])
def SignIn():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']['mail']
    password = data['params']['password']

    employee = EmployeeController.query_byMail(userMail)
    if employee:
        if userMail == employee.mail and password == employee.password:
            return jsonify({'errCode': '0', 'errMsg': 'OK'})

    return jsonify({'errCode': '-3', 'errMsg': '登录失败'})


@app.route('/api/Download', methods=['GET', 'POST'])
def Download():
    return send_from_directory(os.path.join(os.getcwd(), r'static/download'), filename="GetComputerInfo.exe",
                               as_attachment=True)


@app.route('/api/Upload', methods=['POST'])
def Upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'errCode': '-1', 'errMsg': 'No file part'})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'errCode': '-1', 'errMsg': 'No selected file'})

        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(os.getcwd(), r'static/upload', str(time.time()) + filename)
            file.save(path)

        return jsonify({'errCode': '0', 'errMsg': 'OK'})


@app.route('/api/DeleteEmployeeInfo', methods=['POST'])
def DeleteEmployeeInfo():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']['mail']
    employee = EmployeeController.query_byMail(userMail)
    if employee:
        EmployeeController.delete(employee)

    return jsonify({'errCode': '0', 'errMsg': 'OK'})


@app.route('/api/SetComputerInfo', methods=['POST'])
def SetComputerInfo():
    data = json.loads(request.get_data(as_text=True))
    computer = ComputerInfoController.query_byMac(data['MACAddress'])
    if not computer:
        computer = ComputerInfo()
    computer.pcNum = 'SINKA106'  # TODO
    computer.ComputerSystemManufacturer = data['ComputerSystem']['Manufacturer']
    computer.ComputerSystemModel = data['ComputerSystem']['Model']
    computer.OperatingSystemCaption = data['OperatingSystem']['Caption']
    computer.Processor = data['Processor']
    computer.PhysicalMemoryManufacturer01 = data['PhysicalMemory'][0]['Manufacturer']
    computer.PhysicalMemoryPartNumber01 = data['PhysicalMemory'][0]['PartNumber']
    computer.PhysicalMemoryCapacity01 = data['PhysicalMemory'][0]['Capacity']
    computer.PhysicalMemoryManufacturer02 = data['PhysicalMemory'][1]['Manufacturer'] if len(
        data['PhysicalMemory']) > 1 else ''
    computer.PhysicalMemoryPartNumber02 = data['PhysicalMemory'][1]['PartNumber'] if len(
        data['PhysicalMemory']) > 1 else ''
    computer.PhysicalMemoryCapacity02 = data['PhysicalMemory'][1]['Capacity'] if len(data['PhysicalMemory']) > 1 else ''
    computer.PhysicalMemoryManufacturer03 = data['PhysicalMemory'][2]['Manufacturer'] if len(
        data['PhysicalMemory']) > 2 else ''
    computer.PhysicalMemoryPartNumber03 = data['PhysicalMemory'][2]['PartNumber'] if len(
        data['PhysicalMemory']) > 2 else ''
    computer.PhysicalMemoryCapacity03 = data['PhysicalMemory'][2]['Capacity'] if len(data['PhysicalMemory']) > 2 else ''
    computer.PhysicalMemoryManufacturer04 = data['PhysicalMemory'][3]['Manufacturer'] if len(
        data['PhysicalMemory']) > 3 else ''
    computer.PhysicalMemoryPartNumber04 = data['PhysicalMemory'][3]['PartNumber'] if len(
        data['PhysicalMemory']) > 3 else ''
    computer.PhysicalMemoryCapacity04 = data['PhysicalMemory'][3]['Capacity'] if len(data['PhysicalMemory']) > 3 else ''
    computer.DiskDriveCaption01 = data['DiskDrive'][0]['Caption']
    computer.DiskDriveSize01 = data['DiskDrive'][0]['Size']
    computer.DiskDriveCaption02 = data['DiskDrive'][1]['Caption'] if len(data['PhysicalMemory']) > 1 else ''
    computer.DiskDriveSize02 = data['DiskDrive'][1]['Size'] if len(data['PhysicalMemory']) > 1 else ''
    computer.DiskDriveCaption03 = data['DiskDrive'][2]['Caption'] if len(data['PhysicalMemory']) > 2 else ''
    computer.DiskDriveSize03 = data['DiskDrive'][2]['Size'] if len(data['PhysicalMemory']) > 2 else ''
    computer.DiskDriveCaption04 = data['DiskDrive'][3]['Caption'] if len(data['PhysicalMemory']) > 3 else ''
    computer.DiskDriveSize04 = data['DiskDrive'][3]['Size'] if len(data['PhysicalMemory']) > 3 else ''
    computer.IPv4Address = data['IPAddress']['IPv4']
    computer.IPv6Address = data['IPAddress']['IPv6']
    computer.MACAddress = data['MACAddress']

    dbSession.add(computer)
    dbSession.commit()

    return jsonify({'errCode': '0', 'errMsg': 'OK'})


@app.route('/api/BindComputerInfo', methods=['POST'])
def BindComputerInfo():
    data = json.loads(request.get_data(as_text=True))
    userMail = data['params']['mail']

    computer = ComputerInfoController.query_byIPv4(request.remote_addr)

    if not userMail:
        return jsonify({'errCode': '-1', 'errMsg': 'Mail Not Found.'})

    employee = EmployeeController.query_byMail(userMail)
    if not employee:
        return jsonify({'errCode': '-2', 'errMsg': 'Employee Not Found.'})

    employee.MACAddress = computer.MACAddress
    EmployeeController.update(employee)

    return jsonify({'errCode': '0', 'errMsg': 'OK'})
