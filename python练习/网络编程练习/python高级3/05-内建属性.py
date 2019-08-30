# 属性访问拦截器
class A(object):
    def __init__(self,b):
        self.b = b
        self.c = "ok"
    def __getattribute__(self, item):
        print(">>>1:%s"%item)
        if item == "b":
            print("log b")
            return "python"
        else:
            temp = object.__getattribute__(self,item)
            print(">>>2:%s"%str(temp))
            # 调用方法时候,返回方法才能调用 获取show对应的结果 是方法
            return temp
    # 方法内部禁止使用self.xxx方法
    def show(self):
        print("this is itcast")
a = A("python")
print(a.b)
print(a.c)
a.show()
# 先指向再调用
# log日志