
def create_num(all_num):
    a, b = 0,1
    current_num = 0
    while current_num < all_num:
        # 如果一个函数中,有yield，这就不是函数,变成了生成器的模版
        yield a
        a, b = b, a+b
        current_num += 1
    return "ok"
# 如果调用函数发现,函数中有yield,则不是调用函数,而是在创建生成器对象
obj2 = create_num(20)
while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        # 捕获到异常对象的value属性
        print(ret.value)
        break
# 生成器是一种特殊的迭代器
# for num in obj:
#   print(num)