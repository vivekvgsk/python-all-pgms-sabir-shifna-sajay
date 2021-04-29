num1=int(input("enter first number="))
num2=int(input("enter second number="))
num3=(int(input("enter third number=")))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print(" second largst number is=",num2)
    else:
        print("second largest number is=",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("second largst number is=",num1)
    else:
        print("seocnd largest number is=",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("second largst number is=",num1)
    else:
        print("second largset number=",num2)
