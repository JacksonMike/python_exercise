import threading
import time
def test1(temp):
    temp.append(12222)
    print("in test1 %s"%str(temp))
def test2(temp):
    print("in test2 %s"%str(temp))

b = [11,22,33]
def main():               #target 指定函数 args传递参数
    t1 = threading.Thread(target=test1,args=(b,))
    t2 = threading.Thread(target=test2,args=(b,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("in main %s"%str(b))
if __name__ == '__main__':
    main()