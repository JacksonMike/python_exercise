# a = 100
a = [12]  # 可变数据类型可以直接修改


def Test(num):
    num += num
    print(num)


Test(a)
print(a)
