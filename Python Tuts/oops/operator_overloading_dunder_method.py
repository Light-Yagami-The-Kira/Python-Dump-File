class A:
    def __init__(slef,leaves = 0):
        slef.leaves = leaves

    def __add__(a,b):
        return a.leaves + b.leaves
    
    def __repr__(self) -> str:
        return f"I have {self.leaves} leaves."

a = A(12)
b = A()

print(a,b,sep='\n')
print(a+b)
