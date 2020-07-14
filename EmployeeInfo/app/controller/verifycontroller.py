from app.models.models import VerifyInfo
from app.models import dbSession


class VerifyController:
    @staticmethod
    def add(mail, code):
        vi = VerifyInfo()
        vi.mail = mail
        vi.verifyCode = code
        dbSession.add(vi)
        dbSession.commit()

    @staticmethod
    def query_byMail(mail):
        vi = dbSession.query(VerifyInfo).filter(VerifyInfo.mail == mail).one()
        return vi

    @staticmethod
    def delete(mail):
        vi = VerifyController.query_byMail(mail)
        dbSession.delete(vi)
        dbSession.commit()
