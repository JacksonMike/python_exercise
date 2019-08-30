
# 解耦
class Store(object):
    def selectCar(self):
        pass
    def order(self,carType):
       return self.selectCar(carType)
#方法定义到基类, 到子类实现

class CarStore(Store):
    def selectCar(self,carType):
        return Factory.selectCarByType(carType)
class BMWCarStore(Store):
    def selectCar(self,carType):
        return BMWCarStore().selectCar(carType)



class Factory(object):
    def selectCarByType(carType):
        if carType == "宾利":
            return Bentley
        if carType == "兰博基尼":
            return Lamborghini
        if carType == "保时捷"


class BMWFactory(object):
    def selectCarByType(carType):
        if carType == "x5":
            return Bentley
        if carType == "x6":
            return Lamborghini
        if carType == "x7"


class Car(object):
    def move(self):
        print("车移动")
    def stop(self):
        print("车停止")
class Bentley(Car):
    pass
class Lamborghini(Car):
    pass
class Porsche():
    pass
c = CarStore()
c.order()
car = c.order("兰博基尼")
car.move()
car.stop()
