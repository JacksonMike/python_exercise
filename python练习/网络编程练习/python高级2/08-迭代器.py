# 判断是否可以迭代
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))
print(isinstance(100,Iterable))
# 判断是否为迭代器
print(isinstance((x*2 for x in range(9)),Iterator))
# iter()函数
print(isinstance(iter([]),Iterator))
print(isinstance([],Iterator))
# 加了iter()函数后都可以成为迭代器
