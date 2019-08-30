class Cat:
    ''' 定义了一个cat类 '''
    #初始化对象
    def __init__(self,newName,newAge):
        #print("hihihhihhiihihii")
        self.name = newName
        self.age = newAge
    #调用init方法时候self指向创建的对象
    #返回创建对象的引用，并让tom保存
    #方法
    def eat(self):
        print("Cat is eating fish")
    def drink(self):
        print("Cat is drinking")
    def introduce(self):
        print("%s的年龄是:%d" % (self.name, self.age))
#创建一个新的对象
tom = Cat("汤姆",40)
#定义一个cat类 申请内存，执行cat类 返回引用对象 用tom接受创建对象的引用
tom.eat()
tom.drink()
#调用tom变量指向cat的方法
#tom.age = 12
#tom.name = "汤姆"
#给tom指向的对象添加两个属性
tom.introduce()
#print("%s的年龄是:%d"%(tom.name,tom.age))
#获取属性的第一种方式
buleCat = Cat("蓝猫",34)
#buleCat.name = "蓝猫"
#buleCat.age = 13
buleCat.introduce()
print("="*50)
print(tom)
print(buleCat)
