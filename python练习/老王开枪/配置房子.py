class Home:
    def __init__(self,newArea,newKind,newAddress):
        self.area = newArea
        self.kind = newKind
        self.address = newAddress
        #剩余面积开始时候是等于初始面积
        self.leftArea = newArea
        self.containItems = []
    def __str__(self):
        msg= "房子的总面积是:%d,可用面积是:%d,类型是:%s,地址是:%s"%(self.area,self.leftArea,self.kind,self.address)
        msg += "当前房子里的物品有%s"%(str(self.containItems))
        return msg
    def addItem(self,item):
        #item 指向bed1 bed2  self指向房子
       # self.leftArea -= item.area
       # self.containItems.append(item.name)
       self.leftArea -= item.getArea()
        #房子的面积减去床的面积
       self.containItems.append(item.getName())
class Bed:
    def __init__(self,newName,newArea):
        self.name = newName
        self.area = newArea
    def __str__(self):
        return "%s占用的面积是:%d"%(self.name,self.area)
    def getArea(self):
        return self.area
    def getName(self):
        return  self.name
House = Home(300,"高档别墅","深圳市 福田区 香蜜湖 666号")
print(House)
bed1 = Bed("席梦思",4)
print(bed1)
House.addItem(bed1)
print(House)
bed2 = Bed("三人床",5)
print(bed2)
House.addItem(bed2)
print(House)
