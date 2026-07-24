list2=[]
def inputlist():
    n=int(input("enter number"))
    for i in range (n):
        item=int(input("enter elements"))
        list.append(item)
    print("original list: ",list)
def linear_search(list1):
    target=int(input("enter target element: "))
    for l in range(len(list1)):
        if list1[l]==target:
            print("element is found in the list at position: ",l)
    print("element absent")
inputlist()
linear_search(list2)