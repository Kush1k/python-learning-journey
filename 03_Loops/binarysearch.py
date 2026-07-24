list1=[]
n=int(input("enter the number of elements in the list:"))
def inputacceptance():
            for i in range (n):
                item=int(input("enter the element:\n"))
                list1.append(item)
            print("original list is:", list1)

def bubblesort(list2):
        for l in range(0,len(list2)-1):
                
                for j in range(0,len(list2)-l-1):
                    if list2[j]>list2[j+1]:
                        list2[j], list2[j+1] = list2[j+1], list2[j]
        return list2
def binarysearch(list1,element):
        low=0
        high=len(list1)-1
        while (low<=high):
            mid=(low+high)//2
            if (element==list1[mid]):
                print("element found at: ",mid,"index")
                return
            elif(element>list1[mid]):
                low=mid+1
            else:
                high=mid-1
        print("ELEMENT NOT FOUND:\n")

inputacceptance()   
element=int(input("Enter the element you wanna search for:\n"))
bubblesort(list1)
print("sorted list is:", list1)
binarysearch(list1,element)