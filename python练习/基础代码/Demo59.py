#!/usr/bin/python
def Test(a, b, func):
    result = func(a, b)
    return result


A = input("请输入一个函数:")
A = eval(A)  # 等价于 lambda x,y:x-y 去掉引号
num = Test(2, 3, A)  # 匿名函数
print(num)
