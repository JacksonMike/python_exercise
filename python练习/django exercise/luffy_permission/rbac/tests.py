from django.test import TestCase

# Create your tests here.

import random

S = "石头"
J = "剪刀"
B = "布"
allList = [S, J, B]
ManWinList = ([S, J], [J, B], [B, S])
MAN = input("请输入石头、剪刀、布:")
PC = random.choice(allList)
if MAN not in allList:
    print("出手错误，退出游戏")
    exit()
print("电脑出了："), PC
if MAN == PC:
    print("平手！")
elif [MAN, PC] in ManWinList:
    print("你赢了！")
else:
    print("你输了！")
