import re
n="vivek"
x='\w{5}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")