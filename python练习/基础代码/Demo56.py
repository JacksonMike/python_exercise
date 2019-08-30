a = 100
b = a
print(id(a))  # 4306454624
print(id(b))  # 4306454624

A = [22, 33, 44, 55]
B = A
A.append(11)
print(B)

h = [33, 44, 23]
h[0] = 1
g = {"name": "Jim"}
g["name"] = "Tom"
print(g)
print(h)
# 列表和字典是可变数据类型
