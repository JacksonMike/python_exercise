import time
from multiprocessing import Process
def test():
    while True:
        print("test")
        time.sleep(1)
p = Process(target=test)
p.start()
while True:
    print("main")
    time.sleep(1)

