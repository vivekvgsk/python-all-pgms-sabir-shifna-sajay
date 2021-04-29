class Stud:
    course="Python"
    def stdata(self,id,name,mark):
        self.id=id
        self.name=name
        self.mark=mark
class Stud2(Stud):
    def printval(self):
        print("Student id is:",self.id)
        print("Student name is:",self.name)
        print("student course is:",Stud.course)
        print("student mark is:",self.mark)
obj=Stud2()
obj.stdata(10,"Vivek",85)
obj.printval()

