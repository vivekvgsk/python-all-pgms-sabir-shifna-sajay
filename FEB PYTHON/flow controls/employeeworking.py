age=int(input("enter your age:-"))
sex=input("enter your sex (M/F):-")

mstatus=input("are you married or not (Y/S):-")
if(sex=="F"):
    print('work in urban area')
elif(sex=="M")&(40>age>20):
    print("work any where")
elif((sex=="M")&(60>age>40)):
    print("work in urban areas")
else:
    print("ERROR")