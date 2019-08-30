class Dog:
    #当对象完全死去,方法才会调用
    def __del__(self):
        print("It is over")
#引用记数
dog1 = Dog()
dog2 = dog1
del dog1   #不会调用__del__方法,因为这个对象还有其他变量指向他,即引用计数不为0
del dog2   #此时会调用__del__方法，没有变量指向该对象，引用计数为0
print("="*70)
#如果本程序结束时,有些对象还存在,那么python解释器会自动调用__del__方法来完成清理工作
#测量引用计数的方式
class T:
    pass
t = T()
sys.getrefcount(t)