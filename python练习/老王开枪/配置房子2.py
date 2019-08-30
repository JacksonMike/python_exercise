class Home():
    def __init__(self,new_area,new_kind,new_address):
        self.area = new_area
        self.kind = new_kind
        self.address = new_address
        self.left_area = new_area
        self.contain_items = []
    def __str__(self):
        m = "房子的总面积是%d,房子的可用面积是%d,房子的类型是%s,房子的地址是%s,当前房屋里的物品有%s"%(self.area,self.left_area,self.kind,self.address,str(self.contain_items))
        return m
    def addItems(self,item):
        self.left_area -= item.getArea()
        self.contain_items.append(item.getName())
class Bed():
    def __init__(self,new_area,new_name):
        self.area = new_area
        self.name = new_name
    def __str__(self):
        return "%s占用的面积是%d"%(self.name,self.area)
    def getArea(self):
        return self.area
    def getName(self):
        return self.name
h = Home(800,"别墅","香蜜湖")
print(h)
b = Bed(100,"席梦思")
h.addItems(b)
print(h)