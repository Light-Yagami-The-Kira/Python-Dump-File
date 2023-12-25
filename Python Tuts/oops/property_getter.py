class Employee:
    def __init__(self, fn, ln) -> None:
        self.fname = fn
        self.lname = ln
        
    def explain(self):
        return f"This Employee is {self.fname} {self.lname}."
    
    @property
    def printEmail(self):
        return f"{self.lname.lower()}.{self.fname.lower()}@quasarx.com"
    
    @printEmail.setter
    def printEmail(self, string):
        names = string.split('@')[0]
        self.fname = names.split('.')[1]
        self.lname = names.split('.')[0]

    @printEmail.deleter
    def printEmail(self):
        self.fname, self.lname = "",""


a = Employee("Ajay", "Devgun")
b = Employee("Vimal", "Rajnigandha")

print(a.explain(), a.printEmail)
print(b.explain(), b.printEmail)

a.fname = "Krishanu"
b.fname = "Elon"

print(a.explain(), a.printEmail)
print(b.explain(), b.printEmail)

a.printEmail = 'gupta.krishn@quasarx.com'
print(a.explain(), a.printEmail)

del a.printEmail
print(a.explain(), a.printEmail)