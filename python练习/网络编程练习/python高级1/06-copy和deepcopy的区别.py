import copy
a = [11,22]
b = [44,55]
c = [a,b]
e = copy.copy(c)
a.append(99)
print(e)
print(c)
print(id(e))
print(id(c))
# copy拷贝生成了新的空间,但是还是指向原来的引用
print("="*50)
# copy拷贝对可变类型和不可变类型

# 元组为不可变类型,没有产生新的地址
m = (99,33)
n = copy.copy(m)
print(id(m))
print(id(n))
