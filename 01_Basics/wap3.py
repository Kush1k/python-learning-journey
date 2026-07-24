print("Enter number to check for palindrome:")
nums=[]
nums.append(input("Enter number 1: "))
nums.append(input("Enter number 2: "))
nums.append(input("Enter number 3: "))
nums.append(input("Enter number 4: "))
nums.append(input("Enter number 5: "))
numcopy=nums.copy()
numcopy.reverse()
if numcopy==nums:
    print("The numbers are palindrome")
else:
    print("The numbers are not palindrome")