# 全局变量的位置:函数调用之前,函数之外
a = 1


def test():
    print("a=%d" % a)


def test1():
    print("b=%d" % b)


b = 12
test()
test1()
