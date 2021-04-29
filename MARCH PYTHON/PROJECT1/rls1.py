import re
x="[abc]"
count=0
matcher=re.finditer(x,'a52c @x2z')
for match in matcher:
    print("match available at:",match.start())
    print("group=",match.group())
    count+=1
print("count:",count)