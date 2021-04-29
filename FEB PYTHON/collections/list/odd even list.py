lst=[]
odd=[]
even=[]

for i in range(50,201):
    lst.append(i)

for i in lst:
    if(i%2==0):
        even.append(i)

    else:
        odd.append(i)
print(lst)
print(odd)
print(even)