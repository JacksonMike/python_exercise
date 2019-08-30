from threading import Thread
import time
def test1():
    a = 100
    a += 1
    print("in test1 a=%d"%a)
    time.sleep(2)
    print("in test1 a=%d"%a)
def test2():
    time.sleep(1)
    a = 100
    print("in test2 a=%d"%a)
p1 = Thread(target=test1)
p1.start()
p2 = Thread(target=test2)
p2.start()
