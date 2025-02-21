class A:
    def __init__(self):
        stringA="I am in class A"
        print(stringA)
class B(A):
    def __init__(self):
        stringB="I am in class B"
        print(stringB)
        super().__init__()
class C(B):
    def __init__(self):
        stringC="I am in class C"
        print(stringC)
        super().__init__()

c1=C()
