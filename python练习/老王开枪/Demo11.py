class Cat:
    #初始化对象
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge
    def __str__(self):
        return "%s的年龄是:%d"%(self.name,self.age)
    def introduce(self):
        print("%s的年龄是:%d"%(self.name,self.age))
T = Cat("Tom",12)
print(T)

class Animal:
    def __init__(self,newA,newB):
        self.A = newA
        self.B = newB
    def __str__(self):
        return "%s的年龄是:%d"%(self.A,self.B)
    #魔方方法,打印return返回的数据
C = Animal("Jack",12)
print(C)

class Bird:
     def __init__(self,newName):
         self.name = newName
     def printName(self):
         print("名字为:%s"%self.name)
def myPrint(Bird):
    Bird.printName()
dog1 = Bird("Kity")
myPrint(dog1)
