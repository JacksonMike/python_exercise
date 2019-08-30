names = ["Jim","Tom","Sam"]#定义一个列表
names1 = ["Amy","Bob","Cindy"]
a = names + names1 #加号可以加列表
names.extend(a) #将两个列表合并 
names.append("Lily")#直接在后面添加
names.insert(2,"Mary")#数字代表位置，索引号，可以随便插入
print(names)
print(a)