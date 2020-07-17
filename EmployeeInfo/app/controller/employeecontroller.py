from app.models.models import Employee
from app.models import dbSession


class EmployeeController:
    @staticmethod
    def add(mail, password):
        employee = Employee()
        employee.mail = mail
        employee.password = password
        dbSession.add(employee)
        dbSession.commit()
        return employee

    @staticmethod
    def update(user):
        dbSession.add(user)
        dbSession.commit()

    @staticmethod
    def delete(user):
        dbSession.delete(user)
        dbSession.commit()

    @staticmethod
    def query_byMail(mail):
        employee = dbSession.query(Employee).filter(Employee.mail == mail).first()
        return employee
