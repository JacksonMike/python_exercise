

a = [11,22]
b = a
# 指向
print(id(a))
print(id(b))
# 浅拷贝,没有产生新的地址

# 深拷贝,两份
import copy
c = copy.deepcopy(a)
print(id(c))
a.append(8)
print(a)
print(b)
print(c)