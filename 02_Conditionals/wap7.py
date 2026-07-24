def odd_even(num):
    if(num%2==0):
        x=True
    else:
        x= False
    if (x==True):
        print("number is even")
    else:
        print ("number is odd")

num=int(input("Enter your number:"))
odd_even(num)