

def w(fn):
    print("装饰器开始起作用")
    def inner():
        print("验证权限")
        fn()
    return inner
# python解释器执行到这个代码,就会进行自动装饰,而不是调用的时候才进行装饰
@w
def f1():
    print("f1")
# 调用f1()之前已经开始进行装饰
f1()
