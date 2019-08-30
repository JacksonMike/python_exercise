# map函数
ret = map(lambda x:x*x,[1,2,3])
for temp in ret:
    print(temp)


ret2 = map(lambda x,y:x * y,[11,22],[44,55])
for temp in ret2:
    print(temp)


def f1(x,y):
    return (x,y)
a = [1,2]
b = ["m","n"]
c = map(f1,a,b)
for temp in c:
    print(temp)
# filter过滤
ret3 = filter(lambda x:x > 160,[183,156,198])
for temp in ret3:
    print(temp)
ret4 = filter(None,"hello")
for temp in ret4:
    print(temp)
# reduce函数 累加
from functools import reduce
ret5 = reduce(lambda x,y:x+y,[1,2,3,4])
ret6 = reduce(lambda x,y:x+y,[1,2,3],9)
print(ret5)
print(ret6)

# sorted排序
# 默认从小到大
b = sorted([11,33,44,5])
print(b)