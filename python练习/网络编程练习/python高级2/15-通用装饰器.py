def p(fun):
    def inner(*args,**kwargs):
        xxx = fun(*args,**kwargs) # 保存返回的hello
        return xxx
    return inner
@p
def A():
    return "hello"
@p
def B():
    print("world")
@p
def C(a):
    print("%d"%a)
ret = A()
print("%s"%ret)
ret1 = B()
print("%s"%ret1)
C(9)