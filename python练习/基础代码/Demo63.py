class Cat:
    def introduce(self):
        print("%s的年龄是:%d" % (self.name, self.age))


B = Cat()
B.name = "J"
B.age = 12
print(B.name)
print(B.age)
