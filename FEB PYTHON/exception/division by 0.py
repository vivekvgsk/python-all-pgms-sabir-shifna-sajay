a=int(input("enter a number:"))
b=int(input("enter a number:"))
try:
    ans=a/b
    print("answer is:",ans)

except:
    print("division by zero is not possible, please enter a non zero number")
    