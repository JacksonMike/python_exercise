from multiprocessing import Process
import time
def test():
    for i in range(5):
        print("test")
        time.sleep(1)
p = Process(target=test)
# 让这个进程开始执行test函数代码
p.start()