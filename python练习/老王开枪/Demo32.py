#异常处理之抛出异常
class Test(object):
    def __init__(self,switch):
        self.switch = switch #开关
    def calc(self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("已经捕获到异常,信息如下:")
                print(result)
            else:
                #重新抛出异常,异常处理没有被捕获,触发默认异常处理
                raise
a = Test(True)
a.calc(11,0)
print("="*50)
a.switch = False
a.calc(34,0)
