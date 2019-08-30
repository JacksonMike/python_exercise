class Jim(object):
    def order(self,money):
        if money > 3000:
            return Tom()
class Tom(object):
    def move(self):
        print("He is moving")
j = Jim()
t = Jim().order(1000000)
t.move()
