import os
import time

ret = os.fork()
if ret == 0:

    print("1")
else:

    print("2")

ret = os.fork()
if ret == 0:
    print("111")
else:

    print("222")
# 第一个fork:父进程 子进程
# 第二个fork:第一个父进程(父进程,子进程);第一个子进程(父进程,子进程);

