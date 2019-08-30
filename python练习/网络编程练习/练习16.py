# -*- coding:utf-8 -*-
from multiprocessing import Pool
import os,time,random
def work(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    # 生成0-1之间的随机数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕,耗时%0.2f"%(t_stop-t_start))
# 定义线程池,最大线程数3
po = Pool(3)
for i in range(0,10):
    # 要调用的目标,传递的参数
    po.apply_async(work,(i,))
    # 每次循环用空闲出来的子进程调用目标
print("---start---")
# 关闭线程池
po.close()
# 等待所有子线程完成
po.join()
print("---end---")