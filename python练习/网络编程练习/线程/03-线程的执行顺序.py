import threading
import time
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = self.name + "@" + str(i)
            print(msg)
def main():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    main()
# 线程执行顺序和操作系统有关,和线程创建顺序无关