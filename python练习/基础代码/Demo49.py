a = 100


# 全局变量
def test1():
    print("%d" % a)


def test2():
    print("%d" % a)


test1()
test2()

# 定义一个全局变量
temperature = 10


def getTemperature():
    global temperature  # 修改全局变量
    temperature = 33


def printTemperature():
    print("温度是:%d" % temperature)


getTemperature()
printTemperature()
