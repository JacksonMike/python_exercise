def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print("ret2:",ret)
        a, b = b, a+b
        current_num += 1
    return "ok...."
obj = create_num(10)
ret = next(obj)
print(ret)
ret2 = obj.send(None)
print(ret2)


