# coding=utf-8

from pymongo import *

# 获得客户端链接
client = MongoClient("mongodb://w1:456@localhost:27017/work1")
# 切换数据库
db = client.work1
# 获取集合
stu = db.stu
# 修改数据
stu.update_one({"name": "Tom"}, {"$set": {"name": "Tony"}})
