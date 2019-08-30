def foo():
    x = 1

    def inner():
        print(x)

    return inner


func = foo()
# 判断是否为闭包, None则不是, (<cell at 0x102add348: int object at 0x100957d00>,)
print(func.__closure__)
func()
"""闭包函数:内层函数应用了外层函数的环境变量，这样得函数叫闭包函数"""
