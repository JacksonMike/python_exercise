from threading import Thread,Lock
a = 0
# 两个线程都在抢着执行,如果一方抢到这个锁,另一方就会拥塞,直到锁被解开,另一方才能执行
# 加锁后一般多任务变成单任务
def test1():
    global a
    #上锁
    mutex.acquire()
    for i in range(1000000):
        a += 1
    #解锁
    mutex.release()
    print("in test1 a=%d"%a)
def test2():
    global a
    mutex.acquire()
    for i in range(1000000):
        a += 1
    mutex.release()
    print("in test2 a=%d"%a)
# 创建一把互斥锁,默认没有上锁
mutex = Lock()
p1 = Thread(target=test1)
p1.start()
p2 = Thread(target=test2)
p2.start()
print("a=%d"%a)
