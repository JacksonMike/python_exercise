a = [11, 34, 56, 63, 234, 4]
a.sort(reverse=True)
print(a)


def Test(a, b, func):
    result = func(a, b)
    return result


num = Test(2, 3, lambda x, y: x + y)  # 匿名函数
print(num)
