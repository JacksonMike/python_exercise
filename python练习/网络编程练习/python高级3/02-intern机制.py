a = "abc"
b = "abc"
print(id(a))
print(id(b))
del a
del b
e = "abc"
print(id(e))
# 地址不变还是同一个对象,只是指向发生了改变
h = "hello world"
j = "hello world"
print(id(j))
print(id(h))
del h
del j
k = "hello world"
print(id(k))
# 但是字符串中含有空格的没有启动intern机制,仍然会产生新的地址,可以用终端就行验证

