class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a,"+",self.b,"=",self.a+self.b)
    def sub(self):
        print(self.a,"-",self.b,"=",self.a-self.b)
    def mul(self):
        print(self.a,"*",self.b,"=",self.a*self.b)
    def div(self):
        print(self.a,"/",self.b,"=",self.a/self.b)
obj=Calculator(5,2)
obj.add()
obj.sub()
obj.mul()
obj.div()

