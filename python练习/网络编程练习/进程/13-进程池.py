from multiprocessing import Pool
import os
import time
def work(num):
    for i in range(3):
        print("pid = %d,num = %d"%(os.getpid(),num))
        time.sleep(1)
# 进程池中最多有三个任务在执行
pool = Pool(3)
for i in range(10):
    print("%d"%i)
    '''
    向进程池中添加任务,如果添加的任务超过线程池的执行的个数
    则空闲的任务将等到线程池将之前进入的任务做完后再进入,因
    此,所有任务都会被做到
    '''
    pool.apply_async(work,(i,))
# 关闭进程池,不再添加新的任务
pool.close()
# 阻塞 主进程创建任务,任务完成后,立马结束
pool.join()