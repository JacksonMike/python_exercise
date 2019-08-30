def test():
    print("1")
def test():
    print("1000")
test()
# 转向转到第二个


#装饰器原理
def w1(func):
    def inner():
        print("验证权限")
        if True:
            func()
        else:
            print("没有权限")
    return inner
@w1
def f1():
    print("f1")
@w1
def f2():
    print("f2")
f1()
f2()
# 语法糖
# f1 = w1(f1)