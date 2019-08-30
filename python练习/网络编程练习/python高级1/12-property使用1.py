class T(object):
    def __init__(self):
        self.__num = 100
    def setNum(self,newNum):
        self.__num = newNum
    def getNum(self):
        return self.__num
    a = property(getNum,setNum)
t = T()
t.a = 9   # 相当于t.setNum(9)
print(t.a) # 相当于t.getNum()