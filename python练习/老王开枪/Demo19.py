class base(object):
    def test(self):
        print("----test----")
class A(base):
    def test1(self):
        print("---test1---")
class B(base):
    def test2(self):
        print("---test2---")
class C(A,B):
    #多继承
    def test3(self):
        print("---test3---")
c = C()
c.test1()
c.test2()
c.test3()
c.test()
print("-------------------------")

class Jim(object):
    def test(self):
        print("A")
class M(Jim):
    def test(self):
        print("B")
class N(Jim):
    def test(self):
        print("V")
class H(M,N):
    pass
h = H()
h.test()
print(H.__mro__)
#(<class '__main__.H'>, <class '__main__.M'>, <class '__main__.N'>, <class '__main__.Jim'>, <class 'object'>)
#当类中出现了相同的方法,继承顺序,C3算法
