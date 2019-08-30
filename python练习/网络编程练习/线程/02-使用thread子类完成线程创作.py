from threading import Thread
import time
def sing():
    print("唱歌")
    time.sleep(1)
for i in range(5):
    t = Thread(target=sing)
    t.start()
print("="*50)
# 第二种
import threading
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            msg = "I am " + self.name + " @" + str(i);
            print(msg)
            time.sleep(1)
def main():
    t = MyThread()
    # 通过开启start自动调用父类中的run方法
    t.start()
if __name__ == '__main__':
    main()

