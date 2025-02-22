def search():
    val=False
    searchR=input("Enter the roll number you want to search ")
    with open("Student.txt","r") as record:
        Lis=record.readlines()
        for i in Lis:
            temp=i.split(":")
            for searchR in temp:
                print("Found")
                val=True
                break
            else:
                print("Record Not Found")
            if(val==True):
                break
search()