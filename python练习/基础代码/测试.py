print(2 ** 4)
a = '100'
b = int(a)
print("a=%d" % b)

c = '10.444'
d = float(c)
print("c=%f" % d)

age = 12
if age >= 12:
    print("Go home")
age = input("Please input age:")
age1 = int(age)
if age1 >= 13:
    print("Go bar")
else:
    print("Go home")
score = 87
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
else:
    print("C")
