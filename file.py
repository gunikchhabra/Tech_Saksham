diction={}
List=[]
clg="Dronacharya College of Engineering "
class Student:
    def __init__(self):
        self.name=None
        self.rollNo=None
        self.branch=None
    def initialize(self):
        self.name=input("Enter Name: ")
        self.rollNO=int(input("Enter Roll Number: "))
        self.branch=input("Enter Branch: ")


n=int(input("Enter number of Students: "))
for i in range(0,n):
    obj=Student()
    obj.initialize()
    List=((obj.name,obj.branch))
    print(List)
    diction[obj.rollNO]=List
    print(diction)

file=open("Student.txt","a")
for key, value in diction.items():
    file.write(f"{key} : {value}")
    file.write("\n")
file.close()

file=open("Student.txt","r")
print(file.read())
file.close()



    



        
