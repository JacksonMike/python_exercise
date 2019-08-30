import threading
import time
b = 0
def test(a):
    global b
    for i in range(a):
        b += 1
    print("in test b=%d"%b)
def test1(a):
    global b
    for i in range(a):
        b += 1
    print("in test1 temp=%d"%b)
def main():
    t = threading.Thread(target=test,args=(100000,)) #  元组,必须加上逗号
    t1 = threading.Thread(target=test1,args=(100000,))
    t.start()
    t1.start()
    time.sleep(5)
    print("---in--the--main thread b=%d"%b)
if __name__ == '__main__':
    main()