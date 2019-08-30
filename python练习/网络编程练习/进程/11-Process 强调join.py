from multiprocessing import Process
import time
import random
def test():
    for i in range(random.randint(1,5)):
        print("%d"%i)
        time.sleep(1)
p = Process(target=test)
# 让这个进程开始执行test函数代码
p.start()
# 堵塞 等子进程结束,再继续
p.join()
print("main")