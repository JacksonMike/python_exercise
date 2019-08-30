# coding=utf-8

from pymongo import *

# 获得客户端链接
client = MongoClient("mongodb://w1:456@localhost:27017/work1")
# 切换数据库
db = client.work1
# 获取集合
stu = db.stu
# 查询数据
cursor = stu.find()
for s in cursor:
    print(s)

print("="*100)
cursor = stu.find_one()
print(cursor)
print("*"*10000)
cursor = stu.find().skip(1).limit(1)
for s in cursor:
    print(s)
print("#"*10)
cursor = stu.find().sort("age", -1)
for s in cursor:
    print(s)
print("&"*10)
# 多个属性排序
cursor = stu.find().sort[({"age", -1}, {"name", -1})]
for s in cursor:
    print(s)
