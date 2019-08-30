class Animal():
    def eat(self):
        print("吃饭")
class Dog(Animal):
    pass
d = Dog()
d.eat()
# 动态创建类
Cat = type("Cat",(Animal,),{})
c = Cat()
c.eat()
print("="*50)
print(Animal.__class__)
print(Dog.__class__)
print(Cat.__class__)
print(d.__class__)
print(c.__class__)

