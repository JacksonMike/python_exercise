import multiprocessing
import threading
import time
def work():
    while True:
        print("1")
        time.sleep(1)
def make():
    while True:
        print("2")
        time.sleep(1)
def main():
    p1 = multiprocessing.Process(target=work)
    p2 = multiprocessing.Process(target=make)
    p1.start()
    p2.start()
if __name__ == '__main__':
    main()