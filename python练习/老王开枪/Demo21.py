class Tool():
    #属性
    num = 0#类属性 属于类对象 多个实例属性之间共享一个类属性
    #方法
    def __init__(self,newName):
        #实例属性 
        self.name = newName
        #获取类属性
        Tool.num += 1
t1 = Tool("锄头")#实力属性和具体的实列对象有关 一个实力对象与另一个实力对象之间不能共享类属性
t2 = Tool("镰刀")
t3 = Tool("斧头")
print(Tool.num)