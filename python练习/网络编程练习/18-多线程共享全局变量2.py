import threading
import time
def test(temp):
    temp.append(33)
    print("in test temp=%s"%str(temp))
def test1(temp):
    print("in test1 temp=%s"%str(temp))
b = [11,22]
def main():
    # target指定线程将来去哪个函数执行代码
    # args指定将来调用函数时,传递的数据
    t = threading.Thread(target=test,args=(b,)) #  元组,必须加上逗号
    t1 = threading.Thread(target=test1,args=(b,))
    t.start()
    time.sleep(1)
    t1.start()
    time.sleep(1)
    print("---in--the--main thread b=%s"%str(b))
if __name__ == '__main__':
    main()