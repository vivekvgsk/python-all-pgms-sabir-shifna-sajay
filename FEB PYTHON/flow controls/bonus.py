salary=int(input("enter your salary="))
exp=int(input("enter your year of service"))

if(exp>=5):
    bonus=salary*5/100
    print("your Bonus is=",bonus)
else:
    print("you are not Eligible for bonus")