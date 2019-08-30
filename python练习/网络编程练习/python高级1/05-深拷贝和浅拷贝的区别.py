import copy
a = [11,33]
b = [22,44]
c = [a,b]
d = c
print(id(d))
print(id(c))
e = copy.deepcopy(c)
print(id(e))
a.append(100)
print(d)
print(e)
# 另外开辟内存空间的同时,同时指向了新的对象