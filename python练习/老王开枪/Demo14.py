class Animal:
    pass
dog = Animal()
dog.age = 20
print(dog.age)

class Bob:
    #私有属性
    def setAge(self,newAge):
        if newAge > 0 and newAge < 100:
            self.age = newAge
        else:
            self.age = 0
    def getAge(self):
        return self.age
a = Bob()
a.setAge(-12)
age = a.getAge()
print(age)
print("="*60)
class Jim:
    #私有方法
    def __Test(self):
        print("-------发短信吧--------")
    #公有方法
    def Test(self,newMoney):
        if newMoney > 100:
            self.__Test()
        else:
            print("拜拜")
j = Jim()
j.Test(120)
