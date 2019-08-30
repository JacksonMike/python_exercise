import multiprocessing
import time
import os
def test():
    while True:
        print("in 子进程%d 父进程%d"%(os.getpid(),os.getppid()))
        time.sleep(1)
def test1():
    while True:
        print("in 子进程二%d 父进程%d"%(os.getpid(),os.getppid()))
        time.sleep(1)
def main():
    print("in 主进程%d 父进程%d"%(os.getpid(),os.getppid()))
    p1 = multiprocessing.Process(target=test)
    p2 = multiprocessing.Process(target=test1)
    p1.start()
    p2.start()
if __name__ == '__main__':
    main()