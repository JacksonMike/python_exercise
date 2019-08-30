import functools
# 偏函数只需要传一次参数,参数都在里面
def A(*args,**kwargs):
    print(args)
    print(kwargs)
p1 = functools.partial(A,1,2,4)
p1()
p1(5,3,4)
p1(a = "python",b= "itcast")

# wraps函数
import functools
def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print("note something")
        return func()
    return wrapper
@note
def test():
    "test function"
    print("This is test")
test()
print(help(test))
