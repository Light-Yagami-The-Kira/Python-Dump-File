class A:
    def met(self):
        print("Class A")
class B(A):
    def met(self):
        print("Class B")
class C(A):
    def met(self):
        print("Class C")
class d(C,B):
    pass
class D(C,B):
    def met(self):
        print("Class D")

a = d()
b = D()

print(a.met(), b.met(), sep='\n')