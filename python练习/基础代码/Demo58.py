'''nums = [11,22,44,32,12,83,90]
#nums.sort(reverse = True) #从大到小排序
nums.reverse()#逆序
print(nums)
'''

infors = [{"name": "Jim", "age": 12}, {"name": "Tom", "age": 11}, {"name": "Cook", "age": 13}]
infors.sort(key=lambda x: x["age"])  # 匿名函数的应用 按年龄排
print(infors)


def Test(a, b, func):
    result = func(a, b)
    return result


num = Test(2, 3, lambda x, y: x + y)  # 匿名函数
print(num)
