class A(object):
    def __init__(self):
        a = 100
        print(a)


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
# 属性查找
print(dir(D))
# 新式类 D (B,C) A 有object 广度优先
# 旧式类 D B A 深度优先
print("="*200)

