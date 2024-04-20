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

skillf = Employee("Skill", "F")
print(type(skillf))
print(skillf.printEmail)
print(type(skillf.printEmail))

print("================")
print(dir(list()))

print(id(skillf))

print("================")

import inspect
print(inspect.getmembers(skillf))