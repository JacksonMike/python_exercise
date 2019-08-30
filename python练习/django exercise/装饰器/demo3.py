# def index():
#     print("this is index")
#
#
# def login():
#     user = input("user:")
#     pwd = input("pwd:")
#     if user == "Jim" and pwd == "123":
#         print("success")
#         index()
#     else:
#         print("failure")
#
#
# login()

# 封闭开放原则

# def login(func):
#     user = input("user:")
#     pwd = input("pwd:")
#     if user == "Jim" and pwd == "123":
#         print("success")
#         func()
#     else:
#         print("failure")
#
#
# def index():
#     print("this is index")
#
#
# login(index)


def login(func):
    def inner():
        user = input("user:")
        pwd = input("pwd:")
        if user == "Jim" and pwd == "123":
            print("success")
            func()
        else:
            print("failure")

    return inner


@login
def index():
    print("this is index")


# l = login(index)
# l()

index()

