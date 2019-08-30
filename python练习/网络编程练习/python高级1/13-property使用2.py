class T(object):
    def __init__(self):
        self.__num = 100
    @property
    def Money(self):
        return self.__num
    @Money.setter
    def Money(self,newNum):
        self.__num = newNum
t = T()
t.Money = 8
print(t.Money)