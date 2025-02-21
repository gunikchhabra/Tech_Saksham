freq={}
data=input("Enter elements of Array: ").split(",")
print(data)
for i in range(0,len(data)):
    if(data[i] in freq):
        freq[data[i]]+=1
    else:
        freq[data[i]]=1
print(freq)
   
for i in freq:
    if(freq[i]>1):
        print(i)



