def add(a,b=10):
    return a+b
print(add(9))
print(type(add))
func = lambda a,b : a+b
print(func(8,8))
def f(el):
    return el*el
List=[1,2,3,4,5,6]
List2= list(map(f,List))
print(List2)