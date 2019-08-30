import threading
import time
nums = [11,22,33]
a = 99
def test():
    nums.append(1111)
def test2():
    global a
    a += 1
print(a)
print(nums)
test()
print(nums)
test2()
print(a)
# 在函数中对全局变量的指向进行修改时候,如果让全局变量指向了一个新的地方,就要使用global
# 如果仅仅修改了指向空间中的数据,则不需要glboal

print("="*50)
a = 1000
def test3():
    global a
    a += 8
    print("---test3---%d"%a)
def test4():
    print("---test4---%d"%a)
def main():
    t1 = threading.Thread(target=test3)
    t2 = threading.Thread(target=test4)
    t1.start()
    time.sleep(2)
    t2.start()
    time.sleep(2)
    print("---main thread---a=%d"%a)
if __name__ == '__main__':
    main()
# 子线程与子线程共享全局变量