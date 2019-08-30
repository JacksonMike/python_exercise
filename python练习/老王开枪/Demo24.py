class Dog(object):
    def __init__(self):
        print("init method")
    def __del__(self):
        print("del method")
    def __str__(self):
        print("str method")
        return "对象的描述信息"
    def __new__(cls): #cls 此时是dog指向的类对象
        print(id(cls))
        print("new method")
        return object.__new__(cls)
print(id(Dog))
d = Dog()
#调用__new__方法创建对象,然后找一个变量来接受__new__的返回值,这个返回值表示创建出来的对象的引用
#__init__刚刚创建出来对象的应用
#返回对象的引用
#构造方法 new方法创建 init方法初始化