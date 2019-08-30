class Potato:
    def __init__(self):
        self.cook_level = 0
        self.cook_string = "生的"
        self.condiments = []
    def __str__(self):
        return "土豆的状态%s,烤%d分熟,添加的佐料有%s"%(self.cook_string,self.cook_level,str(self.condiments))
    def cook(self,cook_time):
        self.cook_level += cook_time
        if self.cook_level >=0 and self.cook_level < 3:
            self.cook_string = "生的"
        if self.cook_level >= 3 and self.cook_level <6:
            self.cook_string = "半生不熟"
        if self.cook_level >=6 and self.cook_level < 9:
            self.cook_string = "熟了"
        if self.cook_level >=9 and self.cook_level < 12:
            self.cook_string = "烤糊了"
    def add_condiments(self,item):
        self.condiments.append(item)
p = Potato()
p.cook(1)
p.add_condiments("芝麻酱")
print(p)
p.cook(1)
p.add_condiments("辣椒酱")
print(p)
p.cook(1)
p.add_condiments("番茄酱")
print(p)
p.cook(1)
print(p)
p.cook(1)
print(p)
p.cook(1)
print(p)
p.cook(1)
print(p)
p.cook(1)
print(p)
p.cook(1)
print(p)
p.cook(1)
print(p)
p.cook(1)
print(p)
p.cook(1)
print(p)
