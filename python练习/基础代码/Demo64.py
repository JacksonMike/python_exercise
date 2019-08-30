class Car:
    def __init__(self):
        self.wheelNum = 4
        self.color = "bule"


B = Car()
print("车的颜色是:%s" % B.color)


class Animal:
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge


C = Animal("Tom", 12)
print(C.name)
print(C.age)
print(C)
