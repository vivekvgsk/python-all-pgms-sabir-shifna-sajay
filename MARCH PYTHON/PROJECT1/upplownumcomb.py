import re
x=input("enter the word:")

rule="[a-zA-Z]+\d{1}$"
matcher=re.fullmatch(rule,x)
if matcher is not None:
    print("The word is valid")
else:
    print("The word is invalid")