import mysql.connector
print("*"*20 + " WELCOME " +"*"*20)
def signup(data):
    try:
        con=mysql.connector.connect(host='localhost',user='root',password='Gunik@2109',database='dceBatch')
        cur=con.cursor()
        cur.execute(f'select * from STrecord where RollNo={data[0]};')
        result=cur.fetchone()
        if result:
            con.close() 
            return False
        else:
            cur.execute('insert into STrecord(RollNo,Name,password,branch,admissionYR,per_10,per_12) values (%s,%s,%s,%s,%s,%s,%s);',data)
            con.commit()
            con.close()
            return True
        print(cur.fetchall())
        con.close()
    except Exception as e:
        print(e)
while(True):
    print("1. Sign-In ")
    print("2. Sign-Up ")
    print("3. Search ")
    print("4. Display All ")
    print("5. Filter ")
    print("6. Exit ")
    ch=int(input("Enter Choice "))
    if(ch==6):
        print("Thanks for your Time ! ")
        break
    elif(ch==1):
        pass
    elif(ch==2):
        RollNo=int(input("Enter your roll number "))
        Name=input("Enter your Name ")
        Password=input("Enter your Password ")
        Branch=input("Enter your Branch ")
        Per_10=float(input("Enter your 10th standard percentage "))
        Per_12=float(input("Enter your 12th standard percentage "))
        if(signup((RollNo,Name,Password,Branch,Per_10,Per_12))):    #Passing data as a tuple
            print("Student registered Successfully ")
        else:
            print("Student Already Exists")
    elif(ch==3):
        pass
    elif(ch==4):
        pass
    elif(ch==5):
        pass

