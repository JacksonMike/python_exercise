import threading
import time
a = 0
def test1(num):
    global a
    mutex.acquire()
    for i in range(num):
        a += 1
    mutex.release()
    print("in test1 %d"%a)
def test2(num):
    global a
    mutex.acquire()
    for i in range(num):
        a += 1
    mutex.release()
    print("in test2 %d"%a)
mutex = threading.Lock()
def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(5)
    print("in main %d"%a)
if __name__ == '__main__':
    main()