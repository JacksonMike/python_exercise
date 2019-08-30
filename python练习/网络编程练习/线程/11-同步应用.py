from threading import Lock,Thread
from time import sleep
# 多个线程有序执行
class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("task1")
                sleep(1)
                lock2.release()
class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("task2")
                sleep(1)
                lock3.release()
class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("task3")
                sleep(1)
                lock1.release()
# 默认状态没有上锁
lock1 = Lock()
lock2 = Lock()
# lock2上锁
lock2.acquire()
lock3 = Lock()
# lock3上锁
lock3.acquire()
t1 = Task1()
t2 = Task2()
t3 = Task3()
t1.start()
t2.start()
t3.start()