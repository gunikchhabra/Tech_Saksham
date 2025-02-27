class parent:
    def __init__(self):
        self.x=10 # parent variable is not accessible in child class bcz when you create a child class's object then child class constructor will be called but parent class's constructor have to be called  
        print("Parent")
class child(parent):
    def __init__(self):
        self.y=20
        print("Child")
        super().__init__() 
p1=parent()
c1=child()  
print(c1.x)
print(c1.y)                