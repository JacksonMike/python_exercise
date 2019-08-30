class A(object):
    def __new__(cls):
        print("创建对象,分配空间")
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        print("初始化")
a = A()
print(a)
b = A()
print(b)
print("="*50)
class B(object):
    #创建对象的引用
    instance = None
    #初始化动作
    init_flage = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        if not B.init_flage:
            print("初始化")
            B.init_flage = True
c = B()
print(c)
d = B()
print(d)
