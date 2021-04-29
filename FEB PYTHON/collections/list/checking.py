lst=[10,20,30,40,50]
number1=int(input("enter an element"))
flag=0
for i in lst:
    if(i==number1):
        flag=1
        break
    else:
        pass
if(flag>0):
    print("element found")
else:
    print("element not found")