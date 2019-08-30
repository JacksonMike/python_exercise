from threading import Thread
import time
def work(nums):
    nums.append(44)
    print("in work",nums)
def make(nums):
    time.sleep(1)
    print("in make",nums)
g_nums = [11,22,33]
t1 = Thread(target=work,args=(g_nums,))
t1.start()
t2 = Thread(target=make,args=(g_nums,))
t2.start()
