import re
f1=open("python","a")
x="([L][U][M]/d{2}[[P][Y][0-9]{3}$)"
f=open("lumregno","r")

for lines in f:
    number=lines.rstrip("\n")

    matcher = re.fullmatch(x, number)
    if matcher is not None:
        f1.write(number)
        f1.write("\n")
