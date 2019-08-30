card = []
def print_menu():
    print("="*50)
    print("名片信息管理系统")
    print("2,增加一张名片")
    print("3,删除一张名片")
    print("4,修改一张名片")
    print("5,查询一张名片")
    print("6,显示所有名片")
    print("7,退出系统")
def A():
    #增加
    a = input("请输入您的名字:")
    b = input("请输入您的手机号:")
    c = input("请输入您的国籍:")
    new_infor = {}
    new_infor["name"] = a
    new_infor["number"] = b
    new_infor["nation"] = c
    global card
    card.append(new_infor)
    print(card)
def B():
    #查询
    global card
    d = input("请输入要查找的人:")
    f = 0
    for temp in card:
        if d == temp["name"]:
            print("%s\t%s\t%s"%(temp["name"],temp["number"],temp["nation"]))
            f == 1
            break
        if f == 0:
            print("没有找到")
def C():
    #显示
    global card
    print("name\tnumber\tnation")
    for temp in card:
        print("%s\t%s\t%s"%(temp["name"],temp["number"],temp["nation"]))
def D():
    #修改
    pass
def E():
    #删除
    pass
def Main():
    print_menu()
    while True:
        z = int(input("请输入相应的数字:"))
        if z == 2:
            A()
        elif z == 3:
            E()
        elif z == 4:
            pass
        elif z == 5:
            B()
        elif z == 6:
            C()
        elif z == 7:
            break
        else:
            print("您输入的数字有误,请重新输入")
Main()



