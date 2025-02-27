from datetime import date
print("-------------------------Task Manager------------------------------------")
taskList=[]
while(True):
    print("1. Add a task ")
    print("2. Remove a task ")
    print("3.  View all tasks ")
    print("4. Mark a task as task ")
    ch=int(input("Enter a choice : (5 to quit)"))
    if(ch==5):
        break
    elif(ch==1):
        task=input("Enter a task: ")
        taskList.append(task)
        print(taskList)
    elif(ch==2):
        task=input("Enter the task to remove ")
        taskList.remove(task)
        print("Task has been removed ")
        print(taskList)
    elif(ch==3):
        print("Tasks of the day")
        print(taskList)
    elif(ch==4):
        print(taskList)
        task=input("Which task have you completed: ")
        taskList.remove(task)
        print("Yay! you have completed the task")