import time


def timer(func):
    def inner(x, y, *args, **kwargs):
        s1 = time.time()
        func(x, y, *args, **kwargs)
        s2 = time.time()
        print("cost", s2 - s1)

    return inner


# @timer
# def add():
#     ret = 1
#     for i in range(1, 10001):
#         ret += i
#     print(ret)
#
#
# add()

print("hello world")


@timer
def plus(a, b):
    return a + b


plus(10, 99999999999999999)
