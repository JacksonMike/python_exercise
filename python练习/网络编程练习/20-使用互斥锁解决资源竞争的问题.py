import threading
import time
b = 0
def test(a):
    global b
    # 上锁,如果之前没有上锁,默认上锁成功
    # 如果已经上锁,则会堵塞在这里,直到锁解开
    for i in range(a):
        mutex.acquire()
        b += 1
        mutex.release()
    print("in test temp=%d"%b)
def test1(a):
    global b
    for i in range(a):
        mutex.acquire()
        b += 1
        mutex.release()
    print("in test1 temp=%d"%b)
# 创建一个互斥锁,默认没有解锁
mutex =threading.Lock()
def main():
    t = threading.Thread(target=test,args=(100000,)) #  元组,必须加上逗号
    t1 = threading.Thread(target=test1,args=(100000,))
    t.start()
    t1.start()
    time.sleep(3)
    print("---in--the--main thread b=%d"%b)
if __name__ == '__main__':
    main()