list1=[]
n=int(input("enter the number of elements in the list:"))
def inputacceptance():
        for i in range (n):
            item=int(input("enter the element:\n"))
            list1.append(item)
        print("original list is:", list1)
def selectionsort(list2):
      for l in range(len(list2)):
            min_index=l
            for j in range(l+1,len(list2)):
                  if list2[j]<list2[min_index]:
                        min_index=j
            list2[l],list2[min_index]=list2[min_index],list2[l]
inputacceptance()
selectionsort(list1)
print("sorted list is: ",list1)