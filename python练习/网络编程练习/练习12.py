a = 100
b = [11,22]
def test():
    global a
    a += 100
def test1():
    b.append(9999)
test()
test1()
print(a)
print(b)