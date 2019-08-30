def test():
    a = 11
    b = 22
    c = 44
    '''
    用一个列表封装三个变量
    d = [a,b,c]
    return d
    #也可以直接返回
    return [a,b,c]
    #也可以返回元组
    return (a,b,c)
    '''
    # 默认封装元组返回的
    return a, b, c


num = test()
print(num)
