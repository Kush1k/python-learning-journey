tup=(1,4,9,16,25,36,49,64,81,100)
searchele=int(input("enter the element to be searched"))
for i in tup:
    if i==searchele:
        print("element found at",tup.index(i))
        break
else:
    print("element not found")