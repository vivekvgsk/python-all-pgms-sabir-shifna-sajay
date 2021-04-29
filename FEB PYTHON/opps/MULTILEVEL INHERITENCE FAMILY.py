class Father:
    def fdata(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation
class Mother(Father):
    def mdata(self,mname,mage,moccupation):
        self.mname = mname
        self.mage = mage
        self.moccupation = moccupation
class Child(Mother):
    def cdata(self,cname,cage,coccupation):
        self.cname = cname
        self.cage = cage
        self.coccupation = coccupation
class Family(Child):
    def familydata(self):
        print("Father's Name is:",self.name)
        print("Father's Age is:",self.age)
        print("Father's Occupation is:",self.occupation)
        print("Mather's Name is:", self.mname)
        print("Mather's Age is:", self.mage)
        print("Mather's Occupation is:", self.moccupation)
        print("Child's Name is:", self.cname)
        print("Child's Age is:", self.cage)
        print("Child's Occupation is:", self.coccupation)
obj=Family()
print("***************FAMILY DETAILS***************")
obj.fdata("Gangadharan",56,"Carpenter")
obj.mdata("Sindhu",45,"Housewife")
obj.cdata("Vivek",27,"Student")
obj.familydata()
