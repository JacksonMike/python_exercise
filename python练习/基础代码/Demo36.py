a = [{"name": "Jim", "age": 12}, {"name": "Tom", "age": 11}, {"name": "Jack", "age": 10}]
b = input("请输入要查询的名字:")
for temp in a:
    if temp["name"] == b:
        print("找到了")
        break
else:
    print("没找到")
