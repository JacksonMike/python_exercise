i = 1
result = 1
while i <= 9:
    result *= i
    i += 1
print(result)


def getNum(num):
    if num > 1:
        return num * getNum(num - 1)
    else:
        return num


A = getNum(5)
print(A)


def test():
    print("hello")


test()
