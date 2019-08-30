class A(object):
    c_pro = 100

    @classmethod
    def c_met(cls):
        print("world")

    def __init__(self):
        self.obj_pro = 1
        print("python")


a = A()
print(dir(a))
print(dir(A))
"""
通过dir()可以查看调用信息 类不能调用对象属性
"""