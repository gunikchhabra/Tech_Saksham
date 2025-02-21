n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n):
            print("*",sep=" ",end="")
        elif(j==n-i+1):
            print("*",sep=" ",end="")
        else:
            print(" ",sep=" ",end="")
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n):
            print("*",sep=" ",end="")
        elif(j==n-i+1):
            print("*",sep=" ",end="")
        else:
            print(" ",sep=" ",end="")
    print()