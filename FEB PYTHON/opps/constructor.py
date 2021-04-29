class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def printdat(self):
        print("name:",self.name)
        print("age:",self.age)
obj=Person("vivek",26)
obj.printdat()