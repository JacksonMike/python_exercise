
def create_num(all_num):
    print("---1---")
    a, b = 0,1
    current_num = 0
    while current_num < all_num:
        print("---2---")
        # 如果一个函数中,有yield，这就不是函数,变成了生成器的模版
        yield a
        # yield将值传递给num,暂停然后不是从头来,而是继续向下执行.
        print("---3---")
        a, b = b, a+b
        current_num += 1
        print("---4---")
# 如果调用函数发现,函数中有yield,则不是调用函数,而是在创建生成器对象
obj = create_num(10)
obj2 = create_num(2)
ret = next(obj)
print("obj:",ret)
ret = next(obj)
print("obj:",ret)
ret = next(obj2)
print("obj2:",ret)
ret = next(obj)
print("obj:",ret)
ret = next(obj)
print("obj:",ret)
ret = next(obj)
print("obj:",ret)
# 生成器是一种特殊的迭代器
# for num in obj:
#   print(num)