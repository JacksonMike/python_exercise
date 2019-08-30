def A(a, b, *args):
    result = a + b
    for num in args:
        result += num
    print("result=%d" % result)


A(11, 22, 33, 44, 55, 66, 77)
