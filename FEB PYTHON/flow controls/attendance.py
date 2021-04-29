clsheld=int(input("enter total number of classes held:-"))
clsattnd=int(input("total number of class attended"))
per=clsattnd/clsheld*100

if(per>=75):
    print("your attendence percentage is=",per,"so you are eligible for examination")
else:
    print("your attendence percentage is=",per,"so you are not eligible for examination")