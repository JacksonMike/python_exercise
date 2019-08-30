class A(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if A.init_flag:
            return
        print("初始化")
        A.init_flag = True


a = A()
print(a)
b = A()
print(b)
