import random

a = random.randint(0, 2)
scissors = 0
stone = 1
cloth = 2
b = int(input("please input:"))
if a == 1 and b == 2 or a == 0 and b == 1 or a == 2 and b == 0:
    print("win")
elif a == b:
    print("peace")
else:
    print("lose")

m = 1
n = 3
n **= m
print(n)

i = 1
while i <= 4:
    print("H")
    i += 1

j = 1
sum = 0
while j <= 100:
    if j % 2 == 0:
        sum += j
    j += 1
print(sum)
