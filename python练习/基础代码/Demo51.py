a = 1


def test():
    a = 2
    print("a=%d" % a)


def tes1():
    print("a=%d" % a)


test()  # a = 2
tes1()  # a = 1
# 有就用自己的,没有就用全局变量
