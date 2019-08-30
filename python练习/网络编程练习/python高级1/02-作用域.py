#命名空间就是起作用的范围
#查看全局和局部变量
a = 1000
b = 22
print(globals())
def test():
    c = 10
    print(locals())
test()
# LEGB规则(局部 外嵌 全局 内嵌:默认导入的功能)
num = 4
def work():
    num = 5
    def take():
        num = 6
        print(num)
    return take
ret = work()
ret()

#print(dir(__builtin__)) 查看内嵌

