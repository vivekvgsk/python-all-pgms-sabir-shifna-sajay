#import re
#x="a{3}"
#y="aaa abc xyz adf"
#matcher=re.finditer(x,y)
#for match in matcher:
  # print(match.start())
   # print(match.group())

import re
x="a{1,3}"
y="aaa abc xyz adf"
matcher=re.finditer(x,y)
for match in matcher:
    print(match.start())
    print(match.group())