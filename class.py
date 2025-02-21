class A:
    pass #to create an empty class
#to create object of a class
a1 = A() # there is a hidden new method that calls the constructor and initialises the object

class B:
    @staticmethod
    def staticMethod():
        print("I am a static method")
    classVar=10
    def __init__(self,x,y):  #Constructor
            self.x=x
            self.y=y #self is equivalent to this in Js/Java
    def display(self):
        print(self.x)
        print(self.y)
        print("a={} and b={}".format(self.x,self.y))
        #you fill the string using .format self.x 's value will go in curly brace of a
        
b1 = B(21,31)
B.classVar += 10
print(B.classVar)
b1.display()
B.staticMethod()
b1.staticMethod()
# 2 types of variable = instance and class Variable 
# class variable = specific to a class
# instance variable = each one has different value for different instances 
# 2 types of methods = instance and class methods
