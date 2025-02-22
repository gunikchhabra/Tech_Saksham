print("DCE")
student_list_id=[]
students_info={}      
id=26000       
while(True):
    print("1. Admission of Students ")
    print("2. Search ")
    print("3. Terminate the Student ")
    print("4. Display records ")
    ch=int(input("Enter your choice (5 to quit)"))
    if(ch==5):
        break
    elif(ch==1):
        numb = int(input("Enter number of students: "))          
        for i in range (0,numb):
            data = input("Enter data (name,branch,marks) : ").split(",")
            data[2]=int(data[2])
            id=id+1
            students_info[id]=tuple(data)
            student_list_id.append(id)
        print(students_info)
        print(student_list_id)
    elif(ch==2):
        idsearch = int(input("Enter id whose data you want to Search "))
        print(students_info.get(idsearch,"This Student doesn't exist"))
    elif(ch==3):
        idsearch = int(input("Enter id whose data you want to Remove"))
        result = students_info.pop(idsearch)
        if(result):
            student_list_id.remove(idsearch)
            print("Student has been removed")
        else:
            print("No record found")
        print(students_info)
        print(student_list_id)


