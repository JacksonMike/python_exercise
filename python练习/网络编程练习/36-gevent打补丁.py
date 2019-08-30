import gevent
import time
from gevent import monkey
# 将time.sleep 换成 gevent.sleep,即换成相对应的延时操作
# 将程序中用到耗时操作的模块,换成gevent自己实现的模块
monkey.patch_all()
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)
def f2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)
def f3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        time.sleep(0.5)
# 创建的对象放在一个列表里面
gevent.joinall([gevent.spawn(f1,5),gevent.spawn(f2,5),gevent.spawn(f3,5)])
# gevent遇到耗时操作就切换任务
