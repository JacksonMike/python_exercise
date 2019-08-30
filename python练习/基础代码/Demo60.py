a = 5
b = 4
'''
c = 0
c = a
a = b
b = c
print("a=%d,b=%d"%(a,b))
'''
# 变量交换
'''
a = a + b
b = a - b
a = a - b
'''
# 第三种
a, b = b, a
print("a=%d,b=%d" % (a, b))
