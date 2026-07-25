studentlist=[]
def display_student(student):
    print("-------------------------")
    print("ID         :", student["ID"])
    print("Name       :", student["Name"])
    print("Age        :", student["Age"])
    print("Department :", student["Department"])
    print("CGPA       :", student["CGPA"])
    print("-------------------------")
def menu(studentlist):
    while True:
        menuitems="""Options Available are:
        1)Add Student
        2)Display Students
        3)Search Student by ID
        4)Update Student
        5)Delete Student
        6)EXIT
        """
        print(menuitems)
        choice=int(input("Enter your choice: \n"))
        if choice==1:
            print("""Choice is to add student:
            1)Enter Student ID (only integer): 
            2)Enter Student Name: 
            3)Age: 
            4)Department: 
            5)CGPA: 
            """)
            sid=int(input())
            sname=input()
            sage=int(input())
            sdept=input()
            scgpa=float(input())
            studentdict={
                "ID":sid,
                "Name":sname,
                "Age":sage,
                "Department":sdept,
                "CGPA":scgpa
            }
            found=False
            for student in studentlist:
                if student["ID"]==sid:
                    found=True
                    break
            if found:
                print("duplicate ID not allowed")
            else:
                studentlist.append(studentdict)
        elif choice==2:
            if len(studentlist)==0:
                print("No students in the system")
            else:
                print("Students in the system are:")
                for student in studentlist:
                    display_student(student)
        elif choice==3:
            idsearch=int(input("enter the id you want to search for:"))
            found=False
            for student in studentlist:
                idval=student["ID"]
                if idval==idsearch:
                    display_student(student)
                    found=True
                    break
            if not found:
              print("id not found")
        elif choice==4:
            updateid=int(input("Enter the id of student u want to update"))
            found=False
            for student in studentlist:
                updateval=student.get("ID")
                if updateval==updateid:
                    found=True
                    display_student(student)
                    print("""Enter:
                    1)New Age
                    2)New Department
                    3)New Cgpa""")
                    newsage=int(input())
                    newsdept=input()
                    newscgpa=float(input())
                    student["Age"]=newsage
                    student["Department"]=newsdept
                    student["CGPA"]=newscgpa
                    print("Updated student:",student)
                    break
            if not found:
                print("id not found")
        elif choice==5:
            deleteid=int(input("Enter the id of student u want to delete"))
            found=False
            for student in studentlist:
                deleteval=student.get("ID")
                if deleteval==deleteid:
                    found=True
                    print("Student found",student)
                    print("Student will be deleted:")
                    studentlist.remove(student)
                    break
            if not found:
               print("id not found")
        elif choice==6:
            print("exit chosen:")
            break
        else:
            print("invalid Choice Entered")
menu(studentlist)