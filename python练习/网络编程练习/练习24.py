from multiprocessing import Pool
import os,time,random
def work(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕,耗时%0.2f"%(t_stop - t_start))
po = Pool(5)
for i in range(0,15):
    po.apply_async(work,(i,))
print("----start------")
po.close()
po.join()
print("----stop-------")
