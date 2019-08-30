a = []
i = 10
while i <= 77:
    a.append(i)
    i += 1
print(i)
for i in range(10,78):
    print(i)
print(range(1,10000000000))


a = [i for i in range(1,34)]
print(a)
b = [11 for i in range(1,100)]
print(b)
c = [i for i in range(100) if i%2 == 0]
print(c)
d = [i for i in range(2) for j in range(3)]
print(d)
e = [(i,j) for i in range(2) for j in range(3)]
print(e)
f = [(i,j,k) for i in range(2) for j in range(2) for k in range(2)]
print(f)