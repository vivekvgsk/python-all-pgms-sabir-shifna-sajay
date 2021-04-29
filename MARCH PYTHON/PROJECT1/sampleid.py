import re
f=open("studid", 'w')
rule="[0-9]+"
f1=open("id", 'r')
for lines in f1:
    num=lines.rstrip("\n")
    matcher=re.fullmatch(rule, num)
    if matcher!=None:
        f.write(num)
        f.write("\n")