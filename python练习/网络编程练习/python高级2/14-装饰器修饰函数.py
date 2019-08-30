# 对无参数的函数就行修饰
def w(fun):
    def inner():
        print("1234")
        fun()
    return inner
@w
def test():
    print("test")
test()
# 对有参数的函数就行修饰
def v(fun):
    def inner(a,b):
        print("1234")
        fun(a,b)
    return inner
@v
def test1(a,b):
    print("%d %d"%(a,b))
test1(4,5)
# 12行和18行参数个数要相等

# 对不定长参数函数就行修饰
def q(fun):
    def inner(*args,**kwargs):
        print("1234")
        fun(*args,*kwargs)
    return inner
@q
def test2(a,b,c,d):
    print("%d %d %d %d"%(a,b,c,d))
test2(4,5,9,3)

# 对具有返回值的函数就行装饰
def p(fun):
    def inner():
        xxx = fun() # 保存返回的hello
        return xxx
    return inner
@p
def A():
    return "hello"
ret = A()
print(ret)


