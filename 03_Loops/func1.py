def avg(numbers):
    ans=sum(numbers) / len(numbers)
    return ans
numbers=[]
n= int(input("Enter the number of elements: "))
i=0
for i in range(n):
    x=int(input("Enter the numbers: "))
    numbers.append(x)
print("The average is:", avg(numbers))