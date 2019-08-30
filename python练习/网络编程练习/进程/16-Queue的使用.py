from multiprocessing import Queue
from multiprocessing import Process
import time
def write(q):
    for value in ["a","b","c"]:
        print("Put %s to the queue"%value)
        q.put(value)
        time.sleep(1)
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("Get %s from queue"%value)
            time.sleep(1)
        else:
            break;
q = Queue()
qw = Process(target=write,args=(q,))
qr = Process(target=read,args=(q,))
qw.start()
qw.join()
qr.start()
qr.join()
print("所有数据写入并且读完了")