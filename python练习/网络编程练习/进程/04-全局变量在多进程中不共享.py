import os
import time
a = 100
ret = os.fork()
if ret == 0:
    print("process 1")
    a += 1
    print("process 1 a=%d"%a)
else:
    time.sleep(3)
    print("process 2")
    print("process 2 a=%d"%a)
# 主进程生了子进程之后,相当于分家