import pytest
import pymysql
from ReadYml import ReadYml

# @pytest.fixture(scope='function')
# def con_database():
#     # 打开数据库连接
#     db = pymysql.connect("192.168.0.99", "root", "3306", "Auto")
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#     # 使用 execute()  方法执行 SQL 查询
#     cursor.execute("SELECT VERSION()")
#     # 使用 fetchone() 方法获取单条数据.
#     data = cursor.fetchone()
#     print("Database version : %s " % data)
#     # 关闭数据库连接
#     db.close()


# @pytest.fixture(scope='session', autouse=True)
# def clear_yml():
#     ReadYml.clear_yaml()







