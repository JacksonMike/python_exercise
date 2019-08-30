import multiprocessing
import time
import os
a = 1
def test1():
    global a
    a += 1
    print("in 进程1中%d"%a)
    time.sleep(1)
def test2():
    print("in 进程2中%d"%a)
    time.sleep(1)
def main():
    print("in 主进程%d 父进程%d"%(os.getpid(),os.getppid()))
    p1 = multiprocessing.Process(target=test1)
    p1.start()
    p1.join()
    p2 = multiprocessing.Process(target=test2)
    p2.start()
if __name__ == '__main__':
    main()