def sumNums(a, b, c):
    result = a + b + c
    # print("%d + %d + %d = %d"%(a,b,c,result))
    return result


def averageNum(a1, b1, c1):
    result = sumNums(a1, b1, c1)
    result /= 3
    print("平均数是:%d" % result)


num1 = int(input("第一个值是:"))
num2 = int(input("第二个值是:"))
num3 = int(input("第三个值是:"))
sumNums(num1, num2, num3)
averageNum(num1, num2, num3)
