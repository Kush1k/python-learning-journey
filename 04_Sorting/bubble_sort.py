list1=[]
n=int(input("enter the number of elements in the list:"))
def inputacceptance():
        for i in range (n):
            item=int(input("enter the element"))
            list1.append(item)
        print("original list is:", list1)
def bubblesort(list):
      for l in range(0,n-1):
            
            for j in range(0,n-l-1):
                  if list[j]>list[j+1]:
                      list[j], list[j+1] = list[j+1], list[j]
                      return list
inputacceptance()
bubblesort(list1)
print("sorted list is:", list1)
