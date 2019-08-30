nums = [11,22,33]
infor = {"name":"Jim","age":18}
print(len(nums))
print(len(infor)) #键的个数
print(infor.keys())
print(infor.values())
print(infor.items()) #dict_items([('name', 'Jim'), ('age', 18)])元组
for temp in infor.keys():
	print(temp)
for t in infor.items():
	print("key=%s,value=%s"%(t[0],t[1]))
a = (11,22)
b = a
c,d = a #拆包
print(d)
for A,B in infor.items():
	print("key=%s,value=%s"%(A,B))
	