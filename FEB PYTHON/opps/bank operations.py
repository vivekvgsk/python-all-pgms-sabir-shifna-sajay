class Bank:
    bname="SBI" #Static variable
    def acccreat(self,accno,name):
        self.acccno=accno
        self.name=name

        self.minbalance=1000
        self.currbalance=self.minbalance
    def deposit(self,amt):
        self.amt=amt
        self.currbalance+=self.amt
        print("your",Bank.bname,"account has been credited with amt",self.amt)
        print("your current balance is",self.currbalance)
    def withdraw(self,amt):
        self.amt=amt

        if(self.amt>self.currbalance):
            print("insufficeint balance")
        else:
            self.currbalance-=self.amt
            print("Transaction is completed and your current balance is:",self.currbalance)
obj=Bank()
obj.acccreat(100015917,"Vivek")
obj.deposit(25000)
obj.withdraw(5000)