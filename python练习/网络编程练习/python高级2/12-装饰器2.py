# 两个装饰器同时使用
def A(fn):
    def wrap():
        return "<b>" + fn() + "</b>"
    return wrap
def B(fn):
    def wrap():
        return "<i>" + fn() + "</i>"
    return wrap
@A
def test1():
    return " hello world -1 "
@B
def test2():
    return " hello world -2 "
@A
@B #test3 = B(test3)
# 下面的@B先执行
def test3():
    return " hello world -3"
print(test1())
print(test2())
print(test3())
