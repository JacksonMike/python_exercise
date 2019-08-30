import gevent
import time
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(1)
def f2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(1)
def f3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(1)
print("1")
# 创建并开始执行携程
g1 = gevent.spawn(f1,5)
print("2")
g2 = gevent.spawn(f2,5)
print("3")
g3 = gevent.spawn(f3,5)
print("4")
# 等待全部执行
g1.join()
g2.join()
g3.join()
# gevent 遇到耗时操作就切换任务
