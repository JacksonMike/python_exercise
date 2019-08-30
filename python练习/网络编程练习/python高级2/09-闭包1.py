def test():
    print("---1---")
test()
# test变量名指向test()函数,b指向test,所以b也能调用
b = test
b()
print(test)
print(b)
print(id(b))
print(id(test))

print("*"*50)

def T(number):
    print("1")
    def S(number2):
        print("2")
        print(number + number2)
    print("3")
    return S
# ret保存了T的部分代码,所以T并没有结束,并且保存了number的值
ret = T(100)
print("4")
ret(10)