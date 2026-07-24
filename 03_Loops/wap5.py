def listcount(list):
    len_list=len(list)
    return len_list
list=[]
n= int(input("Enter the number of elements: "))
for i in range (n):
    x=int(input("Enter the numbers: "))
    list.append(x)
print("The count is:", listcount(list))
