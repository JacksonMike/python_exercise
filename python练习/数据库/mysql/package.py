# coding=utf8
from pymysql import *


class MySqlHelper(object):
    """封装"""
    def __init__(self, host, port, db, user, passwd, charset="utf8"):
        # 链接mysql的主机
        self.host = host
        # 链接mysql的端口
        self.port = port
        # 链接数据库的名称
        self.db = db
        # 链接的用户名
        self.user = user
        # 链接的密码
        self.passwd = passwd
        # 链接采用的编码方式
        self.charset = charset

    def open(self):
        """建立与数据库的链接"""
        # 创建Collection对象,并传入相关参数
        self.conn = Connection(host=self.host, port=self.port, db=self.db,
                               user=self.user, passwd=self.passwd, charset=self.charset)
        # 调用cursor方法,搜集链接的准备条件
        self.cursor = self.conn.cursor()

    def search(self, sql, params):
        """查找"""
        # 建立链接
        self.open()
        # 传入参数,执行SQL语句
        self.cursor.execute(sql, params)
        # 搜集查询到的信息
        result = self.cursor.fetchall()
        # 关闭链接
        self.close()
        # 返回查询信息
        return result

    def search_one(self, sql, params):
        """查找值返回一个"""
        # 建立链接
        self.open()
        # 传入参数,执行SQL语句
        self.cursor.execute(sql, params)
        # 搜集查询到的信息
        result = self.cursor.fetchone()
        # 关闭链接
        self.close()
        # 返回查询信息
        return result

    def cud(self, sql, params):
        """增删改"""
        # 建立链接
        self.open()
        # 传入参数,执行sql语句
        self.cursor.execute(sql, params)
        # 事物，需要提交才能生效
        self.conn.commit()
        # 关闭链接
        self.close()

    def close(self):
        """关闭与数据库的链接"""
        # 关闭准备条件
        self.cursor.close()
        # 关闭Collection
        self.conn.close()


if __name__ == '__main__':
    # 输入名字
    name = input("please input student name:")
    # 输入序列号
    id1 = input("please input student id:")
    # 格式化名字和序列号
    param = [name, id1]
    # 输入SQL语句
    sql = "update student set name = %s where id = %s"
    # 创建对象
    msh = MySqlHelper("localhost", 3306, "db1", "root", "root")
    # 调用增删改方法
    msh.cud(sql, param)
