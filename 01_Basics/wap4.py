dict1={}
sub1=input("Enter subject name:")
m1=int(input("Enter marks:"))
dict1={sub1:m1}
sub2=input("Enter subject name:")
m2=int(input("Enter marks:"))
dict1.update({sub2:m2})
sub3=input("Enter subject name:")
m3=int(input("Enter marks:"))
dict1.update({sub3:m3})
print("Subject-wise marks:",dict1)