from threading import Thread
import time
import queue
# 创建队列
q = queue.Queue()
class Producer(Thread):
    # 生产者线程
    def run(self):
        count = 0
        while True:
            if q.qsize() < 50:
                for i in range(3):
                    count += 1
                    msg = "产品%d"%count
                    q.put(msg)
                    # 线程号 产品号
                    print("生产者%s生产了一个数据%s"%(self.name,msg))
            time.sleep(0.5)
class Consumer(Thread):
    # 消费者线程
    def run(self):
        while True:
            if q.qsize() > 20:
                for i in range(2):
                    msg = q.get()
                    print("消费者%s消费了一个数据%s"%(self.name,msg))
            time.sleep(1)
for i in range(3):
    p = Producer()
    p.start()
for i in range(5):
    c = Consumer()
    c.start()