class Parent:

    def m1(self):

        print("INSIDE PARENT")

class Child(Parent):
    def m2(self):
        print("INSIDE child class")
class Subchild(Child):
    def m3(self):
        print("INSIDE subchild class")

obj=Subchild()
obj.m1()
obj.m2()
obj.m3()
obj2=Child()
obj2.m2()
obj2.m1()
