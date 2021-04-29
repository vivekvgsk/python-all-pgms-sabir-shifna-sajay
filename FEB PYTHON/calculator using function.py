
print(" choices")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.DIVISION")
print("4.MULTIPLICATION")

choice=int(input("enter your choice"))
num1=int(input("enter your number 1"))
num2=int(input("enter your number 2"))
def addition():
    ans=num1+num2
    print(ans)
def subtraction():
    ans=num1-num2
    print(ans)
def div():
    ans=num1-num2
    print(ans)
def multi():
    ans=num1-num2
    print(ans)
if (choice==1):
    addition()
elif(choice==2):
    subtraction()
elif (choice==3):
    div()
else:
    multi()
