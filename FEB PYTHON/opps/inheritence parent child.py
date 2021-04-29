
#SINGLE INHERITENCE
class Parent:
    parent_name="Vivek"
    def m1(self,age):
        self.age=age
        print("my name is",Parent.parent_name)
        print(self.age)
class Child(Parent):
    def m2(self,cage):
        self.cage=cage
        print("Parent Name is",Parent.parent_name)
        print(self.age)
        print(self.cage)
c=Child()
c.m1(30)
c.m2(12)