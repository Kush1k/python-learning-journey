
Namelist={'KUSHIK','KUMAR','RAJ','RAVI','RAHUL'}
Marklist={90,99,70,44,60}
print("Student name: ", Namelist)
for i in Marklist:
    if i>=90:
        print("Grade A")
    elif i>=80:
        print("Grade B")  
    elif i>=70:
        print("Grade C")
    elif i>=60:
        print("Grade D")
    else:
        print("FAIL")