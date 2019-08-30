from pymongo import *

client = MongoClient("mongodb://make1:123@localhost:27017/make1")
db = client.make1
stu = db.stu
cursor = stu.find()
for s in cursor:
    print(s)
