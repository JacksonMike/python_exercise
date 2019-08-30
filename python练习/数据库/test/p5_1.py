s = 0
count1 = 0
count2 = 0
count3 = 0
avg = 0
while True:
    n = eval(input("Enter an integer, the input ends if it is 0:"))
    if n == 0:
        print("You didn't enter any number")
        break
    else:
        s += n
        count1 += 1
        avg = float(s/count1)
        if n > 0:
            count2 += 1
        else:
            count3 += 1
print("The number of positives is %d" % count2)
print("The number of negatives is %d" % count3)
print("The total is %d" % s)
print("The average is %3.2f" % avg)


