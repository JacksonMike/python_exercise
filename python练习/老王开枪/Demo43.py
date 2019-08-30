a = {11,22,33,11,22,33} #集合
b = [11,22,33,11,22,33]
c = (11,22,33,11,22,33)
print(type(a))
print(c)
print(a)
#去重
d = [11,22,33,44,55,11,22,33]
f =[]
for i in d:
    if i not in f:
        f.append(i)
print(f)
print("="*50)
f = set(a)
print(f)
g = list(f)
print(g)
print("="*50)
h = {11,22,33,44,55}
h.add(10)
print(h)