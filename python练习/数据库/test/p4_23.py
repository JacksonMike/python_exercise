

x, y = eval(input("Enter a point with two coordinates:"))
if x < -5 or x > 5 or y < -2 or y > 2:
    print("point (%2.1f, %2.1f) is not in the rectangle" % (x, y))
else:
    print("point (%2.1f, %2.1f) is in the rectangle" % (x, y))
