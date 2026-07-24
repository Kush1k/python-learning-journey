n= int(input("Enter a numer of elements to count: "))
list=[]
for i in range(n):
    x=int(input("Enter a number: "))
    list.append(x)
print("The sum of the elements in the list is:", sum(list))