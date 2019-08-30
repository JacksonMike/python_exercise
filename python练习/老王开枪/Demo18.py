class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def test1(self):
        print("---test1---")
    def __test2(self):
        print("---test2---")
    def test3(self):
        self.__test2()
        print(self.__num2)
class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)
b = B()
b.test1()
#b.test2()私有方法不会被继承
print(b.num1)
#print(b.num2)私有属性也不会被继承
print("="*50)
b.test3()
#b.test4()
#如果调用的是继承的父类中的共有方法,可以在这个公共方法中访问父类的私有属性和方法.
#但是在子类中实现了一个共有方法，则不能访问父类中的私有属性和方法