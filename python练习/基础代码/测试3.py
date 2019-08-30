import random

player = input("Please input 0剪刀 1石头 2布:")
p = int(player)
computer = random.randint(0, 2)
if ((p == 0 and computer == 2) or (p == 1 and computer == 0) or (p == 2 and computer == 1)):
    print("win")
elif p == computer:
    print("flat")
else:
    print("lose")

i = 0
sum = 0
while i <= 10:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)

j = 1
while j <= 9:
    k = 1
    while k <= j:
        print("%d*%d=%-4d" % (j, k, j * k), end='')
        k += 1
    print('\n')
    j += 1
