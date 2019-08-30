# 函数调用传递局部变量
# 一使用全局字典的方法
import threading
global_dict = {}
# 将s传递到B(),C()中
def A():
    s = 1
    global_dict[threading.current_thread().name] = s
    C()
    B()
def B():
    s = global_dict[threading.current_thread().name]
    print(s)
def C():
    s = global_dict[threading.current_thread().name]
    print(s)
A()
# 第二种使用 threadinglocal
# 设置全局变量local_school
local_school = threading.local()
def process_student():
    std = local_school.student
    print("hello,%s in %s"%(std,threading.current_thread().name))
def process_thread(name):
    # 为local_school添加属性
    local_school.student = name
    process_student()
t1 = threading.Thread(target=process_thread,args=("Jim",),name="Thread-A")
t2 = threading.Thread(target=process_thread,args=("Tom",),name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()

