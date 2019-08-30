import threading
import time
from threading import Thread
def test():
    name = threading.current_thread().name
    print("thread name is %s"%name)
    # 函数内的变量并不共享
    a = 100
    if name == "Thread-1":
        a += 1
    else:
        time.sleep(2)
    print("the thread is %s,a=%d"%(name,a))
p1 = Thread(target=test)
p1.start()
p2 = Thread(target=test)
p2.start()