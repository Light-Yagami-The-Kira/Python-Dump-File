class Employee:
    def __init__(self, name, empID, age, salary = 23443) -> None:
        self.name = name
        self.empID = empID
        self.age = age
        self.salary = salary

    def printDetails(self):
        print(self.name, self.empID, self.age, self.salary)

    @classmethod
    def asString(self,inp):
        params = inp.split('-')
        try: 
            x = Employee(params[0], params[1], params[2],params[3])
        except:
            x = Employee(params[0], params[1], params[2])
        return x
    
    @classmethod
    def func(cls):
        print(cls)
    
Krishanu = Employee("Krishanu Karmakar", 545541, 23)
Krishanu.printDetails()
Krishan = Employee("Krishanu Karmakar", 545541, 23, 1000000)
Krishan.printDetails()
Krisha = Employee.asString("Krishu-123-16")
Krisha.printDetails()

Krisha.func()