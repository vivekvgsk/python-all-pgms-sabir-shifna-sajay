class Emp:
    companyname="LUMINAR TECHNOLAB"
    def empdat(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
    def printdata(self):
        print("your employee id is:",self.id)
        print("your name is:",self.name)
        print("your designation is:",self.designation)
        print("your salary is",self.salary)
        print("Company:",Emp.companyname)
obj=Emp()
obj2=Emp()
obj.empdat(1,"vivek","software developer",25000)
obj2.empdat(2,"shyam","junior software developer",15000)
obj.printdata()
print("***********************************************")
obj2.printdata()