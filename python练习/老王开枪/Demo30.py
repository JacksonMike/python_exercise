def test1():
    print("----a-----")
    print(num)
    print("----b-----")
def test2():
    print("----c------")
    test1()
    print("-----d------")

def test3():
    try:
        print("------e------")
        test2()
        print("------f------")
    except Exception as result:
        print("捕获的信息是:%s"%result)
    print("------h----------")
test3()
print("&&&&&&&&&&&&&&&")
test2()
#异常的传递

