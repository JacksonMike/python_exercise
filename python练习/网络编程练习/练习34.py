from greenlet import greenlet
import time
def T1():
    while True:
        print("1")
        t2.switch()
        time.sleep(1)
def T2():
    while True:
        print("2")
        t1.switch()
        time.sleep(1)
t1 = greenlet(T1)
t2 = greenlet(T2)
t1.switch()
