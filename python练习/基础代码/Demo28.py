a = ["Amy","Jim","Bob","Cindy","Jim","Tom","Sam"]
a.pop()#删除最后一个元素
a.remove("Jim")#删除所选内容，但是只删一次
print(a[0]) #Amy
print(a[-1]) #Tom
print(a[1:3]) #字符串同样适用
print(a)
b = ["Jim","Bob","Cindy","Jim","Tom","Sam"]
del b[1] #根据下标删除
print(b)
