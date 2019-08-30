# coding=utf8
from pymysql import *
from hashlib import sha1


class MySqlHelper(object):
    def __init__(self, host, port, db, user, passwd, charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = Connection(host=self.host, port=self.port, db=self.db,
                               user=self.user, passwd=self.passwd, charset=self.charset)
        self.cursor = self.conn.cursor()

    def search(self, sql, params):
        self.open()
        self.cursor.execute(sql, params)
        result = self.cursor.fetchall()
        self.close()
        return result

    def cud(self, sql, params):
        self.open()
        self.cursor.execute(sql, params)
        self.conn.commit()
        self.close()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    # 接收用户输入的数据
    name = input("请输入名字:")
    pwd = input("请输入密码:")
    # 对密码进行加密,加密方式
    s1 = sha1()
    # 加密数据
    s1.update(bytes(pwd, encoding="utf-8"))
    # 加密后的结果
    pwd = s1.hexdigest()
    # 查询语句
    sql = "select pwd from user where name = %s"
    # 链接数据库
    msh = MySqlHelper("localhost", 3306, "db1", "root", "root")
    # 获取查询结果进行比对
    result = msh.search(sql, [name])
    # (('40bd001563085fc35165329ea1ff5c5ecbdbbeef',),)最终结果
    print(result)
    # 如果结果为空,用户名错误
    if len(result) == 0:
        print("用户名错误")
    elif result[0][0] == pwd:
        print("登陆成功")
    else:
        print("密码错误")
