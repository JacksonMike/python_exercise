# 定义正负两个方向
pos = eval(input("please input pos:"))
# 起始点
start = 0
# 初始往左走一步,然后右走两步
n = 1
# 统计步数之和
s = 0
if pos > 0:
    while start < pos:
        s += n
        if n % 2 == 0:
            start += n
        else:
            start -= n
        n += 1
    print(s)
else:
    while start > pos:
        s += n
        if n % 2 == 0:
            start += n
        else:
            start -= n
        n += 1
    print(s)
