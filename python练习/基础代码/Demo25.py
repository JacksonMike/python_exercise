a = "news"
h = "agMNHIJNMNOPMN"
q = "we hava never given up"
j = h[2:4]  # b包括2，不包括4
k = h[2:-2]  # 倒数第二个.结果HIJ
l = h[2:]  # 一直取到最后
m = h[2:-2:2]  # 2起点  -1终点 2步长：隔几个取
n = h[::-1]  # 逆序
e = a[0]
f = a[len(a) - 1]  # 取最后一个
g = a[-1]  # 取最后一个
b = "paper"
c = a + b
d = "%s" % (a + b)
print(h.find("OP"))  # 字符串开始的地方，从左往右找
print(h.find("MN"))  # 2
print(h.rfind("MN"))  # 从右往左找 8
# print(h.index("S"))ValueError: substring not found 和find功能类似，但是如果没找到，就会出现错误
print(h.index("MN"))
print(h.rindex("MN"))
print(h.count("MN"))  # 统计个数
print(h.count("s"))  # 不存在为0
print(h.replace("a", "A"))  # 前面想替换，后面要替换
print(h)  # 替换后原字符串不变
print(h.replace("MN", "AB", 3))  # 从左往右依次替换，最后一个为替换个数
print(q.split(" "))  # 切割 整句
print(q.capitalize())  # 第一句第一个单词首字母大写
print(q.title())  # 每一个单词首字母都大写
