pattern="ABCDBCA"
dic={}
for i in pattern:
    if(i not in dic):
        dic[i]=1
    else:

         print("first recursive character is:",i)
         print(dic)
         break