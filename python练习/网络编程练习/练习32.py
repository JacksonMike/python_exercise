import time
def task1():
    while True:
        print("---1---")
        time.sleep(0.1)
        yield
def task2():
    while True:
        print("---2---")
        time.sleep(0.1)
        yield
def task3():
    while True:
        print("---3---")
        time.sleep(0.1)
        yield
def main():
    t1 = task1()
    t2 = task2()
    t3 = task3()
    while True:
        next(t1)
        next(t2)
        next(t3)
if __name__ == '__main__':
    main()