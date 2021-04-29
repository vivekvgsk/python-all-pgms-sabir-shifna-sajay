class Stud:
    course="Python"
    def stdata(self,id,name,mark):
        self.id=id
        self.name=name
        self.mark=mark
class Qualification:
    def qual(self,qualf):
        self.qualf=qualf

class Stud2(Stud,Qualification):
    def printval(self):
        print("Student id is:",self.id)
        print("Student name is:",self.name)
        print("His/Her qualification is:",self.qualf)
        print("student course is:",Stud.course)
        print("student mark is:",self.mark)
obj=Stud2()
obj.stdata(10,"Vivek",85)
obj.qual("BCA")
obj.printval()