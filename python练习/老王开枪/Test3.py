num = 1050
def demo1():
    num = 10
    print(num)
    num = 20
    print(num)
def demo2():
    global num
    num = 1
    print(num)
demo2()
print("="*100)
def measure():
    a = 1
    b = 2
    return (a,b)
c = measure()
print(c)
print("="*34)

def demo3(num,num_list):
    num = 1000
    num_list = [1,2]
    num_list.append(5)
    print(num)
    print(num_list)
v = 1
x = [5,3,4]
demo3(v,x)


class Cat:
    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)
    def __del__(self):

        print("%s 去了" % self.name)
    def __str__(self):
        return "我是小猫：%s" % self.name

tom = Cat("Tom")
print(tom)

