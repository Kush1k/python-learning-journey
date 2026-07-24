print("PLEASE ENTER BILL FOR ITEM =1.5$")
billamt=float(input("Enter the bill amount: "))
if (billamt==5 or billamt==1 or billamt==2):
    print("bill is accepted")
    if (billamt>1.5):
        print("bill is accepted, the change is ",billamt-1.5)
    elif (billamt==1.5):
        print("no change is required, thank you")
    else:
        print("bill is accpeted,but amount not enough:")
else:
    print("bill is not allowed for the machine")