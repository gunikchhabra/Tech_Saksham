class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(self.make)
        print(self.model)
        print(self.year)
    def update(self):
        updY=int(input("Enter new Year "))
        self.year=updY
        print("Year has been updated to "+str(self.year))

veh1=vehicle("Car","Kia Seltos",2019)
veh1.display()
veh1.update()
