#字典
a = {"name":"Jim","age":15,"job":"cook"}
print("%s %d %s"%(a["name"],a["age"],a["job"]))
b = [{"name":"Jim","age":18},{"name":"Tom","age":12}]
for temp in b:
	print(temp)
for temp in b:
	print(temp["name"])
