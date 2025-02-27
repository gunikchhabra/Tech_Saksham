class workout:
    def __init__(self):
        self.date=None
        self.exType=None
        self.dur=None
        self.calB=None

    def initialize(self):
        print("Enter Your Work-Out Details: ")
        self.date=input("Enter date (DD-MM-YYYY): ")
        self.exType=input("Enter exercise type: ")
        self.dur=input("Enter the duration: ")
        self.calB=input("Enter calories burnt: ")
        
class user(workout):
    
    def __init__(self):
        self.name=None
        self.age=None
        self.weight=None 
        self.numb=0
        self.Workout=[]
    def input(self):
        self.name=input("Enter your name: ")
        self.age=input("Enter your age: ")
        self.weight=input("Enter your weight (in Kg): ")
    def show(self):
        print(self.name)
        print(self.age)
        print(self.weight)
    def addWorkout(self):
        w=workout()
        w.initialize()
        self.Workout.append(w.date)
        self.Workout.append(w.exType)
        self.Workout.append(w.dur)
        self.Workout.append(w.calB)
    def ViewWorkout(self):
        print(self.Workout)
    def SaveData(self):
        if(self.name==None):
            print("Data has not been added yet !")
        elif(self.numb==0):
            self.numb=1
            fileName=input("Enter File Name: ")
            with open (fileName,"a") as record:
                record.write(f"{self.name}\n")
                for i in self.Workout:
                    print(i)
                    record.write(f"{i}\n")
            record.close()
        else:
            print("You Can't save the data more than once ")

def main():
    ch=0
    while(ch!=5):
        print("1. Add a task")
        print("2. View Tasks")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")  
        ch=int(input("Enter your choice"))
        if(ch==5):
            break
        elif(ch==1):
            u=user()
            u.input()
            u.addWorkout()
        elif(ch==2):
            u.ViewWorkout
        elif(ch==3):
            u.SaveData()
        elif(ch==4):
            


