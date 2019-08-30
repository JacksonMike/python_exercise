class Dog(object):
    __instance = None
    __initFlag = False
    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self,name):
        if Dog.__initFlag == False:
            self.name = name
            Dog.__initFlag = True

a = Dog("Tim")
print(id(a))
print(a.name)
b = Dog("Tom")
print(id(b))
print(b.name)