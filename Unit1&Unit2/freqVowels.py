#Wap to count frequency of vowels
string = input("Enter a string: ")
counta=0
counte=0
counti=0
counto=0
countu=0
List=list(string)
for i in range(0,len(List)):
    if(List[i]=="a"or List[i]=="A" ):
        counta+=1
    elif(List[i]=="e" or List[i]=="E"):
        counte+=1
    elif(List[i]=="i" or List[i]=="I"):
        counti+=1
    elif(List[i]=="o" or List[i]=="O"):
        counto+=1
    elif(List[i]=="u" or List[i]=="U"):
        countu+=1

print("Count of a or A is "+ str(counta))
print("Count of e or E is "+ str(counte))
print("Count of i or I is "+ str(counti))
print("Count of o or O is "+ str(counto))
print("Count of u or U is "+ str(countu))