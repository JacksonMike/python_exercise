i = 1
num = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
        num += 1
    if num == 3:
        continue  # 结束本次循环，再继续进行下一次循环
    i += 1
print("====")
