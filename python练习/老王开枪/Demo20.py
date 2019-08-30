class Dog(object):
    def work(self):
        print("I am a policeman")
class Tom(Dog):
    def work(self):
        print("I am a thief")
def teach(temp):
    temp.work()
d1 = Dog()
d2 = Tom()
teach(d1)
teach(d2)
#多态,定义的时候不确定,只有在调用的时候才确定
#面向对象三大特征:封装 继承 多态