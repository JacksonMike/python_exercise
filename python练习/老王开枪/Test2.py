def test(num):
    print("%x"%(id(num)))
    result = 100
    print("%x"%(id(result)))
    return  result
a = 1
r = test(a)
print("%x"%(id(a)))
print("%x"%(id(r)))
print("="*50)
demo_list = [1,2,3]
print("%x"%(id(demo_list)))
demo_list.append(8)
print("%x"%(id(demo_list)))
print("="*50)
m = (11,22,33,44)
