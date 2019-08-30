import os
import time
# 在这里生成两个进程,第一个(父进程)进程ret>0,第二个(子进程)进程ret=0
ret = os.fork()
if ret == 0:
    while True:
        print("---1---")
        time.sleep(1)
else:
    while True:
        print("---2---")
        time.sleep(1)

