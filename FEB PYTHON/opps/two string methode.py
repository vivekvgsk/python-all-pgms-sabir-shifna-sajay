class College:
    collegename="LT"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def printdata(self):
        print("college name",self.collegename)
        print("name of student",self.name)
        print("roll no",self.roll)
    def __str__(self):
        return self.name+str(self.roll)
ob=College("Anu",5)
print(ob)