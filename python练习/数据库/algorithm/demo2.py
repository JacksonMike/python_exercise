#!/usr/bin/env python 
# coding:utf-8
import sys
import time

# 程序开始时间
start = time.time()


def f(m):
    """递归"""
    if m == 1 or m == 2:
        return 1
    else:
        return f(m - 1) + f(m - 2)


n = 1
# 计数器
count = 0
while f(n) <= sys.maxsize:
    count += 1
    n += 1
print("第%s个斐波拉契数达到最大整数" % count)
# 程序结束时间
end = time.time()
# 耗费时间
cost_time = end - start
print(cost_time)


