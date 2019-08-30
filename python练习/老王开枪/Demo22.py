class Game(object):
    #类属性
    num = 100
    #实例方法
    def __init__(self):
        #实列属性
        self.name = "Jim"
    @classmethod
    #类方法
    def addNum(cls):
        cls.num = 10
    #静态方法
    @staticmethod
    def printMenu():
        print("穿越火线")
g = Game()
#g.addNum()也可以通过类创建出来的对象来调用这个方法
Game.addNum()#可以通过类的名字调用方法
print(Game.num)
Game.printMenu()
g.printMenu()