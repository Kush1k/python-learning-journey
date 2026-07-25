from datetime import datetime
name=input("enter your name: ")
def menu(name):
    while True:
        menuitem=(""" 
        MENU CHOICES:
        1)SAY HELLO
        2)TELL CURRENT TIME
        3)PRINT YOUR NAME 
        4)EXIT """)
        print(menuitem)
        choice=int(input("Enter one of the Choices "))
        if choice==1:
            print("Hello")
        elif choice==2:
            now=datetime.now()
            print(now.time())
        elif choice==3:
            print(name)
        elif choice==4:
            print("exit chosen:")
            break
        else:
            print("invalid choice")
menu(name)