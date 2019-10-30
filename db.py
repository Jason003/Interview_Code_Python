# import sqlite3
# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()
# cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
# cursor.execute("insert into user values (\'1\', \'Jason\')")
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = "user"
	id = Column(String(20), primary_key = True)
	name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:Ljf&4753539@localhost:3306/test?auth_plugin=mysql_native_password')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# session = DBSession()
# new_user = User(id = '5', name = 'Bob')
# session.add(new_user)
# session.commit()
# session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()