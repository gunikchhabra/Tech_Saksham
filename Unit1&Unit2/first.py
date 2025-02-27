#Create
numb = int(input("Enter number of students: "))
student_list_id=[]
students_info={}      
id=26000                 
for i in range (0,numb):
    data = input("Enter data (name,branch,marks) : ").split(",")
    data[2]=int(data[2])
    id=id+1
    students_info[id]=tuple(data)
    student_list_id.append(id)
print(students_info)
print(student_list_id)
#Search
idsearch = int(input("Enter id whose data you want to Search "))
#print(students_info.get(idsearch,"This Student doesn't exist"))

#delete
result = students_info.pop(idsearch)
if(result):
    student_list_id.remove(idsearch)
    print("Student has been removed")
else:
    print("No record found")
print(students_info)
print(student_list_id)
