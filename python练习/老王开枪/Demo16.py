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
    '''
    def eat(self):
        print("---吃---")
    def drink(self):
        print("---喝---")
    def sleep(self):
        print("---睡---")
    def run(self):
        print("---跑---")
    '''
    def bark(self):
        print("---嚎叫---")
class Cat(Animal):
    def catch(self):
        print("---抓老鼠---")
wC = Dog()
wC.eat()
wC.bark()
tom = Cat()
tom.catch()
#不允许tom使用dog中的方法
#wC使用cat中的方法