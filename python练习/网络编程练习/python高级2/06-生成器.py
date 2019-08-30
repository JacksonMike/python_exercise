# 列表生成式
a = [x*3 for x in range(10)]
print(a)
# 生成器第一种创建方式
b = (x*2 for x in range(14))
print(b)
print(next(b))
print("="*50)
# 生成器二
def createNum():
    m,n = 0,1
    for i in range(5):
        yield n
        m,n = n,m+n
print(createNum())
# 接收yield后面的值
a = createNum()
'''for i in a:
    print(i)'''
# ret = a.__next__()
ret = next(a)
print(ret)
# 等价




