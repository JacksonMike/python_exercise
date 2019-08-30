from collections import Iterable
from collections import Iterator
import time
class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0
    def add(self,name):
        self.names.append(name)
    def __iter__(self):
        '''要使一个对象成为一个可以迭代的对象,先要使用for,必须实现__iter__方法'''
        return self
    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration
classmate= Classmate()
classmate.add("Jim")
classmate.add("Tom")
classmate.add("Tony")
print("判断classmate是否为可以迭代的对象:",isinstance(classmate,Iterable))
# 通过iter函数调用classmate实力对像,返回值为Classmate函数中iter方法的返回值
classmate_iterator = iter(classmate) # iter(classmate) = ClassIterator(self)
print("判断class_iterator是否为迭代器:",isinstance(classmate_iterator,Iterator))
print(next(classmate_iterator))
for name in classmate:
    print(name)
    time.sleep(1)