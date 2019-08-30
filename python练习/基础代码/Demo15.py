sex = input("请输入你的性别")
if sex == "M":
	color = input("你白吗")
	money = int(input("你有多少钱"))
	if color == "white" and money >= 1000:
		print("富二代")
	else:
		print("屌丝")
else:
	print("请走吧")