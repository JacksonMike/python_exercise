i = 1
num = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
        num += 1
    if num == 5:
        break  # 跳出循环
    i += 1
print("====")
