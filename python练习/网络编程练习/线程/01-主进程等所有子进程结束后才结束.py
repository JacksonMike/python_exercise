import threading
from time import sleep,ctime
def sing():
    for i in range(3):
        print("唱歌%d"%i)
        sleep(1)
def dance():
    for i in range(3):
        print("跳舞%d"%i)
        sleep(1)
def main():
    print("%s"%ctime())
    # 程序开始就有一条主线程
    # 创建线程1
    t1 = threading.Thread(target=sing)
    # 创建线程2
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    print("%s"%ctime())
    # 当所有子线程结束后,主线程才结束
if __name__ == '__main__':
    main()