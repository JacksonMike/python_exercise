class Person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return "%s,%d"%(self.name,self.weight)
    def run(self):
        print("%s跑步"%self.name)
        self.weight -= 1
    def eat(self):
        print("%s吃饭"%self.name)
        self.weight += 2
Tom = Person("汤姆",70)
Tom.eat()
Tom.eat()
Tom.run()
print(Tom)
Jack = Person("杰克",65)
Jack.run()
Jack.eat()
Jack.eat()
Jack.eat()
print(Jack)

class Women():
    def __init__(self,name):
        self.name = name
        self.__age = 12
    def __secret(self):
        print("%s的年龄是"%(self.__age))
Andy = Women("安迪")
print(Andy._Women__age)
Andy._Women__secret





