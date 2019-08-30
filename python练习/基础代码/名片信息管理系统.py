# 打印功能提示
print("=======================")
print("名字关系信息系统")
print("1:添加一个名字")
print("2:修改一个名字")
print("3:删除一个名字")
print("4:查看一个名字")
print("5:退出系统")
print("======================")

# 名字信息系统

# 定义空列表来存储添加的名字
b = []
while True:
    a = int(input("请输入功能序号:"))

    if a == 1:
        c = input("请输入一个名字:")
        b.append(c)
        print(b)
    elif a == 2:
        x = str(input("请输入要改的名字:"))
        y = b.index(x)
        z = input("请输入修改后的名字:")
        b[y] = z
        print(b)
    elif a == 3:
        h = input("请输入需要删除的名字:")
        b.remove(h)
        print(b)
    elif a == 4:
        d = input("请输入要查询的人名:")
        if d in b:
            print("找到了,有这个人")
        else:
            print("查无此人")
    elif a == 5:
        break
    else:
        print("输错了,请重新输入")
