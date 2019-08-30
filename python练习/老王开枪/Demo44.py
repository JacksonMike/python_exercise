# 名片管理系统
# 用来存储名片
card = []


def printMenu():
    '''完成打印功能菜单'''
    print("=" * 50)
    print("         名片管理系统终极版")
    print("1,添加一张新名片:")
    print("2,删除一张名片")
    print("3,查询一张名片")
    print("4,修改一张名片")
    print("5,显示所有的名片")
    print("6,保存信息")
    print("7,退出系统")
    print("=" * 50)


def A():
    '''完成添加一个新功能的名片'''
    a = input("请输入你的名字:")
    b = input("请输入你的QQ号:")
    c = input("请输入你的微信号:")
    d = input("请输入你的国籍:")
    # 定义新字典,存储新名片
    new_infor = {}
    new_infor["name"] = a
    new_infor["QQ"] = b
    new_infor["WeChat"] = c
    new_infor["nationality"] = d
    global card
    # 将字典添加到列表中
    card.append(new_infor)
    print(card)


def B():
    '''用来查询一个名片'''
    global card
    e = input("请输入你要查找的姓名:")
    f = 0  # 默认表示没找到
    for temp in card:
        if e == temp["name"]:
            print("%s\t%s\t%s\t%s" % (temp["name"], temp["QQ"], temp["WeChat"], temp["nationality"]))
            f = 1  # 表示找到了
            break
    if f == 0:
        print("查无此人")


def V():
    '''显示所有的名片信息'''
    global card
    print("name\tQQ\tWeChat\tnationality")
    for temp in card:
        print("%s\t%s\t%s\t%s" % (temp["name"], temp["QQ"], temp["WeChat"], temp["nationality"]))


def saveToFile():
    # 将已经添加的信息保存到文件中
    f = open("backup.data", "w")
    f.write(str(card))
    f.close()


def load():
    global card
    try:
        f = open("backup.data")
        card = eval(f.read())
        f.close()
    except Exception:
        pass


def Main():
    '''完成对整个程序的控制'''
    # 加载之前的数据到程序中
    load()
    printMenu()
    while True:
        num = int(input("请输入相应的操作序号:"))
        if num == 1:
            A()
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            B()
        elif num == 5:
            V()
        elif num == 6:
            saveToFile()

        elif num == 7:
            break
        else:
            print("您输入的序号有误,请重新输入.")
    print("")


if __name__ == "__main__":
    Main()
