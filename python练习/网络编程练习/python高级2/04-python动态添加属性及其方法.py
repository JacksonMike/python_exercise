a = 100
def T():
    print("hello world")
a = T
a()
print("="*50)
# 添加属性
class Person(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
p = Person("Jack",18)
p.addr = "China"
Person.num = 1000
print(p.name)
print(p.addr)
print(p.num)
# 添加方法
import types
class Animal(object):
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
    def eat(self):
        print("%s吃老鼠"%self.name)
def run(self):
    print("%s跑步"%self.name)
a = Animal("Tom",43)
a.run = types.MethodType(run,a)
xxx = types.MethodType(run,a)
xxx()
a.run()



