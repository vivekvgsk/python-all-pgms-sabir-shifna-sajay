import re

x = '\d{10}'
f=open("sample",'r')
lst=[]
for lines in f:
 match = re.fullmatch(x, lines)
# print(match)
 if match is not None:
  print("valid")
  lst.append(lines)

 else:
  print("invalid")

print(lst)