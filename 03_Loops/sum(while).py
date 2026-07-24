n= int(input("Enter a numer of elements to count: "))
list=[]
i=0
while i<n:
    x=int(input("Enter a number: "))
    list.append(x)
    i+=1
print("The sum of the elements in the list is:", sum(list))