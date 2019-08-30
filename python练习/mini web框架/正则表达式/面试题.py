class Foo(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item, end=" ")
        return self

    def __str__(self):
        return ""

    def __getattribute__(self, item):
        self.dog = 10000


print(Foo().think.take.make)
"""构造一个类Foo
用python的魔法方法实现
class Foo
print(Foo().think.different.itcast.itheima)
think different itcast itheima
__init__
__str__
__new__
__del__
__call__
__repr__

一般不调用,递归
相当于def __getattr__(dog)
def __getattr__(self, item):
    self.dog = 1000

"""