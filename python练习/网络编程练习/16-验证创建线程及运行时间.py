import threading
import time
def test1():
    for i in range(5):
        print("----test1----%d"%i)
        time.sleep(1)

def main():
    # 在调用thread线程之前先打印当前线程的信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)
    # 在调用thread之后打印
    print(threading.enumerate())
    t1.start()
    # 在调用start之后再打印
    print(threading.enumerate())
if __name__ == '__main__':
    main()
# 当调用thread的时候不会创建线程
# 当调用thread创建出来的实列对象时,才会创建线程让这个对象开始运行