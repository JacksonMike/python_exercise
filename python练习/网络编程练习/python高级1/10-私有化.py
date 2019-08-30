class Test(object):
    def __init__(self):
        self.__num = 100
    def setNum(self,newNum):
        self.__num = newNum
    def getNum(self):
        return self.__num
t = Test()
t.setNum(1)
print(t.getNum())



import D
print(D.num)
print(D._num)
print(D.__num)
