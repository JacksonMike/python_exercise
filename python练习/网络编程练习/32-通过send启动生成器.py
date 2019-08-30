
def create_num(all_num):
    a, b = 0,1
    current_num = 0
    while current_num < all_num:
        ret =yield a
        print(">>>ret>>>>",ret)
        a, b = b, a+b
        current_num += 1
obj = create_num(20)
ret = next(obj)
print(ret)
# send不能放到第一次,如果用 obj.send(None)
ret = obj.send(None)
print(ret)
# 首先执行yield = a,将A的值赋予obj,第二部再将None的值赋予yield并且输出,然后a = 1,跳到ret = yield a,
# 将a 的值赋予给obj,程序暂停
