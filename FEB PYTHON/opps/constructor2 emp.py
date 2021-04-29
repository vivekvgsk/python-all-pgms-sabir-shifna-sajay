class Emp:
    companyname="LUMINAR TECHNOLAB"
    def __init__(self,id,name,designation,salary):
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
obj=Emp(1,"vivek","software developer",25000)
obj.printdata()
