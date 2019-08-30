from threading import Thread
import time
# 线程之间共享全局变量
a = 100000
def work():
    global a
    for i in range(100000):
        a += 1
    print("in work a=%d"%a)
def make():
    global a
    for i in range(100000):
        a += 1
    print("in make a=%d"%a)
t1 = Thread(target=work)
t1.start()
t2 = Thread(target=make)
time.sleep(3)
t2.start()
print("a=%d"%a)