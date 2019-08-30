class Tool(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Tool.count += 1
    @classmethod
    def show(cls):
        print("%d"%cls.count)
    @staticmethod
    def make():
        print("H")
a = Tool("锤子")
b = Tool("镰刀")
print("%d"%Tool.count)
Tool.show()
Tool.make()

class A(object):
    def __new__(cls, *args, **kwargs):
        print("h")
        ab = super().__init__(cls)
        return ab
    def __init__(self):
        print("初始化")
a = A()
print(a)
b = A()
print(b)