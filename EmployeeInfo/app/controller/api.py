from app import app
from app.models.models import session
from app.models.models import Employee
from flask import request
import json


@app.route('/api/GetAllEmployeeInfo')
def GetAllEmployeeInfo():
    employees = session.query(Employee).filter(Employee.id == 2).one()
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

    session.add(employee)
    session.commit()
    return 'ok'


@app.route('/api/ApplyVerifyCode', methods=['POST'])
def ApplyVerifyCode():
    data = json.loads(request.get_data(as_text=True))
    mail = data['params']
    print(mail)
    return 'ok'
