# import re
# x="a+"
# y="aaa abc xyz adf"
# matcher=re.finditer(x,y)
# for match in matcher:
#     print(match.start())
#     print(match.group())

import re
x="a*"
y="aaa abc xyz adf"
matcher=re.finditer(x,y)
for match in matcher:
    print(match.start())
    print(match.group())

# import re
# x="a?"
# y="aaa abc xyz adf"
# matcher=re.finditer(x,y)
# for match in matcher:
#     print(match.start())
#     print(match.group())