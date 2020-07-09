from app import app
from app.models.models import session
from app.models.models import Employee
import json


@app.route('/GetAllEmployeeInfo')
def GetAllEmployeeInfo():
    employees = session.query(Employee).filter(Employee.id == 2).one()
    print(employees)
    return employees.name
