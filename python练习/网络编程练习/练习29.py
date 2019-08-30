import time
from collections import Iterable
from collections import Iterator
class Classmate():
    def __init__(self):
        self.names = list()
    def add(self,name):
        self.names.append(name)
    def __iter__(self):
        return ClassIterator(self);
class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
        self.current_num = 0
    def __iter__(self):
        pass
    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration
classmate = Classmate()
classmate.add("Jack")
classmate.add("Jim")
classmate.add("Jane")
print("判断classmate是否为迭代对象",isinstance(classmate,Iterable))
classmate_iterator = iter(classmate)
print("判断classmate_iterator是否为迭代器",isinstance(classmate_iterator,Iterator))
print(next(classmate_iterator))
for temp in classmate:
    print(temp)
    time.sleep(1)




