from collections import Iterable
from collections import Iterator
import time
class Classmate(object):
    def __init__(self):
        self.names = list()
    def add(self,name):
        self.names.append(name)
    def __iter__(self):
        return ClassIterator(self) # 属性传递 Classmate属性传递给 ClassIterator
class ClassIterator(object):
    def __init__(self,obj):
        self.obj = obj
    def __iter__(self):
        pass
    def __next__(self):
        return self.obj.names[2]
classmate = Classmate()
classmate.add("Jim")
classmate.add("Tom")
classmate.add("Kobe")
classmate_iterator = iter(classmate)
print("判断classmate是否为迭代对象:",isinstance(classmate,Iterable))
print("判断classmate_iterator是否为迭代器",isinstance(classmate_iterator,Iterator))
print(next(classmate_iterator))
for name in classmate:
    print(name)
    time.sleep(1)
