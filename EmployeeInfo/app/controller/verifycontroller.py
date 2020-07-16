from app.models.models import VerifyInfo
from app.models import dbSession


class VerifyController:
    @staticmethod
    def add(mail, code):
        if not VerifyController.query_byMail(mail):
            vi = VerifyInfo()
            vi.mail = mail
            vi.verifyCode = code
            dbSession.add(vi)
            dbSession.commit()
        else:
            vi = VerifyController.query_byMail(mail)
            vi.verifyCode = code
            VerifyController.update(vi)

    @staticmethod
    def query_byMail(mail):
        vi = dbSession.query(VerifyInfo).filter(VerifyInfo.mail == mail).one()
        return vi

    @staticmethod
    def update(verifyInfo):
        dbSession.add(verifyInfo)
        dbSession.commit()

    @staticmethod
    def delete(mail):
        vi = VerifyController.query_byMail(mail)
        dbSession.delete(vi)
        dbSession.commit()
