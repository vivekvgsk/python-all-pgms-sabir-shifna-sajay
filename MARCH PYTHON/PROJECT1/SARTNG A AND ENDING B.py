import re
x=input("enter the word:")
rule= "^a[a-zA-Z0-9\W]*b$"
matcher=re.fullmatch(rule,x)
if matcher is not None:
    print("The word is valid")
else:
    print("The word is invalid")