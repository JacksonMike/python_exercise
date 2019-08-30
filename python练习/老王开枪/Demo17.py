class Animal:
    def eat(self):
        print("---吃---")

    def drink(self):
        print("---喝---")

    def sleep(self):
        print("---睡---")

    def run(self):
        print("---跑---")
class Dog(Animal):
    def bark(self):
        print("---汪汪叫---")
class D(Dog):
    def fly(self):
        print("---飞翔---")
    #方法重写
    def bark(self):
        print("---狂叫---")
Kolkie = D()
Kolkie.fly()
Kolkie.bark()
Kolkie.drink()
#多次继承