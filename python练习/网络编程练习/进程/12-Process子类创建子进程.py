import time
from multiprocessing import Process
class MyProcess(Process):
    def run(self):
        while True:
            print("1")
            time.sleep(1)
p = MyProcess()
# 通过start调用父类Process的run方法
p.start()
while True:
    print("main")
    time.sleep(1)