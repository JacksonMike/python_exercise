class T(object):
    num = 100
    print("a")
    def __init__(self):
        self.name = "Jack"
print(T)
print("="*50)
# 添加属性
class S(object):
    a = 100
s1 = S()
print(s1.a)
S2 = type("S2",(),{"a":100}) #类名,继承类名字 ,属性/方法
s2 = S2()
print(s2.a)
print("="*50)
# 添加方法
def work(self):
    print("---num---%d"%self.num)
T3 = type("T3",(),{"work":work})
b = T3()
b.num = 100
b.work()