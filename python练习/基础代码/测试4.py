name = "Jim"
for x in name:
    print("=======")
    if x == "J":
        continue  # 执行后这个循环没用了
    # break直接跳出循环
    print(x)

a = input("Please input name:")
b = str(a)
c = input("Please input code:")
d = int(c)
if b == "Jim" and d == 1234:
    print("Welcom")
else:
    print("Fail")
