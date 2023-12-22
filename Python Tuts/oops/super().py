class A:
    classVar1 = "I am a class variable 1"
    def __init__(self):
        self.var1 = "I am inside Class A's constructor"
        self.classVar1 = "INstance  variable of class A"

class B(A):
    classVar1 = "I am a class variable B"
    def __init__(self):
        super().__init__()
        self.var1 = "xyz"

a = A()
b = B()
    
print(b.classVar1)