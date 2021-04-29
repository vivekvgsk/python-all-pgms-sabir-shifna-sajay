class Student:
    def __init__(self,name,mark):
        self.mark=mark
        self.name=name
    def printvalue(self):
        print("Name:",self.name)
        print("mark:",self.mark)
    def __str__(self):
        return self.name
f=open("student","r")
for line in f:
    data = line.split(",")
    print(data)
    name = data[0]
    mark = data[1]
    ob=Student(name,mark)
    print(ob)
    ob.printvalue()
