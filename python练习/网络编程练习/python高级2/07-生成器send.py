def F(times):
    a,b = 0,1
    n = 0
    while n < times:
        temp = yield b
        print(temp)
        a,b = b,a+b
        n += 1
f = F(9)
ret = next(f)
print(ret)
ret = next(f)
print(ret)
ret = f.send("hello")
print(ret)
# yield起到暂停作用