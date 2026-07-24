def printlist(list,index):
    if (index==len(list)):
        return
    print(list[index])
    printlist(list,index+1)
list1=['Kushik','VISHAK','AKSHATHA','GANESH']
printlist(list1,0)