num1=int(input("enter a number="))
if(num1>1):
    for i in range(2,num1):
        if(num1%i==0):
            print("the number is not a prime")
            break
        else:
            print("the number is prime")
else:
    print("number is not prime")