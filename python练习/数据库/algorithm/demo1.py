#!/usr/bin/env python 
# coding:utf-8
import sys
import time

# 程序开始时间
start = time.time()


def f():
    """迭代"""
    # 第一个斐波拉契数字为1
    a = 0
    b = 1
    # 定义计数器
    count = 0
    # python3中表示最大整数为sys.maxsize
    while b <= sys.maxsize:
        print(b)
        count += 1
        a, b = b, a + b
    print("第%s个斐波拉契数达到最大整数" % count)


f()
# 程序结束时间
end = time.time()
# 耗费时间
cost_time = end - start
print(cost_time)

