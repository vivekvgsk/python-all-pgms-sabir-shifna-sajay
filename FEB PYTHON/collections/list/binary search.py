lst=[100,20,30,40,50]
lst.sort()
print(lst)
low=0
upp=len(lst)-1
element=int(input("enter an element"))
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
            flag=1
            break
if(flag>0):
    print("element found")
else:
    print("element not found")

