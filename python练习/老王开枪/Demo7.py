f = open("Tom.txt","r")
print(f.readline())#一行一行读
print(f.readline())
print(f.readline())
print("="*40)
g = open("Jack.txt")
c = g.seek(1,0)#0表示开头位置,2表示空几格(正数往左,负数往右,但是python3不支持负数,python2支持)seek表示指针位置
print(g.tell())#表示当前指针的位置
print(g.readline())
print(g.tell())
print(g.read())
print(c)