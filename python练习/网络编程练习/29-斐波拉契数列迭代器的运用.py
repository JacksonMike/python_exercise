class F(object):
    def __init__(self,all_num):
        self.all_num = all_num
        self.a = 0
        self.b = 1
        self.current_num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            # 先算等号右边的,算完后把值赋给左边
            self.a,self.b = self.b,self.a+self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration
f = F(30)
for temp in f:
    print(temp)
# 迭代器存储的是生成斐波拉契数列的方法,耗费内存空间小.
# 一般的方式存储的是斐波拉契数列的空间,耗费内存空间打.