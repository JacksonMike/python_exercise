from threading import Thread
import time
a = 0
b = 1
def test1():
    global a
    global b
    if b == 1:
        for i in range(1000000):
            a += 1
        b = 0
    print("in test1 a=%d"%a)
def test2():
    global a
    # 轮询 效率比较低,当上面的线程在执行的时候,下面的线程在判断,仍然在占有CPU做无用攻
    while True:
        if b != 1:
            for i in range(1000000):
                a += 1;
            break
    print("in test2 a=%d"%a)
p1 = Thread(target=test1)
p1.start()
p2 = Thread(target=test2)
p2.start()
print("a=%d"%a)
