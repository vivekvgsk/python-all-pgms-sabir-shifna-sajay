import re
x=input("enter the word:")
rule="[a-zA-Z\W]{8,15}"
matcher=re.fullmatch(rule, x)
if matcher!=None:
    print("valid")
else:
    print("please enter a valid string,Numbers are not allowed")