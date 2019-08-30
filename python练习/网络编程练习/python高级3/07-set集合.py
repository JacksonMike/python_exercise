# 去掉重复
a = [11,22,33,11,22,33]
b = set(a)
print(b)
c = list(b)
print(c)

# 集合运算

D = [11,22,33,44,55,66]
d = set(D)
E = [11,99,88,33]
e = set(E)
print(d&e) #交
print(d|e) #并
print(d-e) #减 减去共有的
print(d^e) #减去共有的加上两者独有的
