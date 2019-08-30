import threading
import time
def test():
    for i in range(5):
        print("---test---%d"%i)
        time.sleep(1)
def main():
    print(threading.enumerate())
    t = threading.Thread(target=test)
    print(threading.enumerate())
    t.start()
    print(threading.enumerate())
if __name__ == '__main__':
    main()
# 当t.start()调用后子线程才开始