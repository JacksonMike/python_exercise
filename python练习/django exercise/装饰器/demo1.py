# x = 12
#
#
# def foo():
#     x = 1
#     print(x)
#     print("OK")
#
#
# foo()
# print(foo.__name__)

"""
LEGB
L —— Local(function)；函数内的名字空间
E —— Enclosing function locals；外部嵌套函数的名字空间(例如closure)
G —— Global(module)；函数定义所在模块（文件）的名字空间
B —— Builtin(Python)；Python内置模块的名字空间
"""


# x = 3
#
#
# def bar():
#     # x = 1
#
#     def inner():
#         # x = 2
#         print(x)
#
#     inner()
#
#
# bar()

# 指向
# def bar():
#     print("bar")
#
#
# foo = bar
# foo()
