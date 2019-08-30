def test(a, d, b=22, c=1):  # b,c为缺省参数
    result = a + b + c + d
    print("result=%d" % result)


test(11, 33, 7)  # 传了用传的,不传用22，不能放在最前面
test(d=22, a=22, b=111)  # b为命名参数


def A(a, b, *args):
    print(a)
    print(b)
    print(args)  # (33, 44, 55, 56)

    result = a + b
    print("result=%d" % result)


A(11, 22, 33, 44, 55, 56)
print("=======================")
# (12,)只有一个元素的元组
A(33, 44, 55)
A(33, 33)  # ()
