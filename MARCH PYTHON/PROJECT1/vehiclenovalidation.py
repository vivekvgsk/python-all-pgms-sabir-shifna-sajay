import re
lst=[]
rule="[Kk][Ll]\d{2}[a-zA-Z]{2}\d{4}$"
f=open("vehregno", "r")
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        lst.append(number)
print(lst)