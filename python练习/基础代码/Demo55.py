def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


A = (1, 2, 3)
B = {"name": "Jim", "age": 12}
test(11, 22, 33, *A, **B)
# 元组* ,字典**
