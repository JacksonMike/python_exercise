from multiprocessing import Pool
import os
import time
def test():
    print("进程池中的进程%d %d"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("%d"%i)
        time.sleep(1)
    return "hello"
def test1(args):
    print("%d"%os.getpid())
    print("%s"%args)
pool = Pool(3)
pool.apply_async(func=test,callback=test1)
time.sleep(3)
print("%d"%os.getpid())