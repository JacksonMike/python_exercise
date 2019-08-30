name = "Mike"


def say_hello():
    print("hello1")
    print("hello2")
    print("hello3")


say_hello()
print(name)


def sum(sum1, sum2):
    result = sum1 + sum2
    return result


m = sum(3, 4)


def A(a):
    a *= 3
    print(a)


A(m)


def test():
    print("=" * 50)


def test1():
    test()
    print("=" * 12)


test1()


def B(char):
    print(char * 3)


B("*")


def C(char, times):
    print(char * times)


C("&", 34)
