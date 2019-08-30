nums = list()
a = 0
b = 1
i = 0
while i < 10:
    a,b = b,a+b
    nums.append(a)
    i += 1
for temp in nums:
    print(temp)