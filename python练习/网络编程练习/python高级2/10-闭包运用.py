def line(a,b):
    def line_in(x):
        print(a*x + b)
    return line_in
line1 = line(1,2)
line1(1)
line2 = line(2,3)
line2(1)
line2(2)
line1(9)
# 开辟了多个内存空间并且没有被释放