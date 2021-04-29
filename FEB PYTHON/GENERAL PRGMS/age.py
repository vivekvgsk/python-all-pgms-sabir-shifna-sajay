date=int(input("enter your date of birth:-"))
month=int(input("enter your month of birth:-"))
year=int(input("enter your year of birth"))

cdate=int(input("enter current date:-"))
cmonth=int(input("enter current month:-"))
cyear=int(input("enter current year:-"))

dt=cdate-date
m=cmonth-month
y=cyear-year
print("your are ",y,"years",m,"months",dt,"days old")
