a = [11,33]
b = [11,33]
c = a
d = 100
e = 100
print(d is e)
f = -127
g = -127
print(f is g)
print(id(a))
print(id(b))
print(id(c))
# is 判断两个对象的引用是否指向同一个对象
print(a is b)
# == 判断两个对象的值是否相等
print(a == b)
print(c is b)