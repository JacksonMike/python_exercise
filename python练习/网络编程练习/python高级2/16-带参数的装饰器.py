
def A(c):
    def w(fun):
        def inner():
            print("%s"%c)
            if c == "bare":
                fun()
                fun()
            else:
                fun()
        return inner
    return w
@A("bare")
def test():
    print("---test---")
test()
# 先执行A()函数,这个函数return的结果是w的这个函数的引用
# @w
# @w对test进行装饰
