import threading
import time
from math import sqrt
a = 1000
def test1():
    global a
    a += 1000
    print("in test1 %d"%a)
def test2():
    print("in test2 %d"%a)
def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t2.start()
    time.sleep(1)
    t1.start()
    time.sleep(1)
    print("in main %d"%a)
if __name__ == '__main__':
    main()
r = float(input("a:"))
print("The area is",3.14*r**2)
print((sqrt(2)*1))