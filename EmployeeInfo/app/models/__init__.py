import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

# 初始化数据库连接:
url = URL(drivername='postgresql', username='postgres', password='123456', host='localhost', database='employeeinfodb')
engine = sa.create_engine(url)

# 创建DBSession类型:
DBSession = sessionmaker(engine)

dbSession = DBSession()

