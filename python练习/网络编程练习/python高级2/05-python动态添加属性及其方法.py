# 添加静态方法和类方法
class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
@classmethod
def test(cls):
    print("---class method---")
@staticmethod
def work():
    print("---static method---")
p = Person("Jim",12)
Person.test = test
Person.test()
Person.work = work
Person.work()

class Dog(object):
    __slots__ = ("name","age")
d = Dog()
d.name = "Jane"
d.age = 10
print(d.age)


