class SweetPotato:
    # 定义初始化方法
    def __init__(self):
        # 描述地瓜的生熟成都
        self.cookedString = "生的"
        # 数字
        self.cookedLevel = 0
        # 地瓜配料
        self.condiments = []
        # 列表,能够存储多个数据

    def __str__(self):
        return "地瓜 状态:%s(%d),添加的佐料有:%s" % (self.cookedString,
                                           self.cookedLevel, str(self.condiments))
        # 打印出列表返回值

    def cook(self, cookedTime):
        # 要多次储存变量的值,把变量的值扔到属性里面来
        self.cookedLevel += cookedTime
        if self.cookedLevel >= 0 and self.cookedLevel < 3:
            self.cookedString = "生的"
        elif self.cookedLevel >= 3 and self.cookedLevel < 5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >= 5 and self.cookedLevel < 8:
            self.cookedString = "熟了"
        elif self.cookedLevel >= 8:
            self.cookedString = "烤糊了"

    def addCondiments(self, item):
        # 列表添加
        self.condiments.append(item)


# 创建一个地瓜对象
dG = SweetPotato()
print(dG)
# 开始烤地瓜
dG.cook(1)
print(dG)
dG.addCondiments("花椒")
dG.cook(1)
print(dG)
dG.cook(1)
dG.addCondiments("味精")
print(dG)
dG.cook(1)
print(dG)
dG.cook(1)
print(dG)
dG.cook(1)
print(dG)
dG.cook(1)
dG.addCondiments("洋葱")
print(dG)
dG.cook(1)
dG.addCondiments("大蒜")
print(dG)
dG.cook(1)
print(dG)
