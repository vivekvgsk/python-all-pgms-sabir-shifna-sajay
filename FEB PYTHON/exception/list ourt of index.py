lst=[10,20,30]
try:
    index = int(input("enter an index value to print"))

    print("The value is:",lst[index])
except:
    print("out of index")
finally:
    print("inside finally")