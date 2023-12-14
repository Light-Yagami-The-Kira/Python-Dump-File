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
    

    @staticmethod
    def Function_of_class_Employee():
        print("Hello i am a static method")
    

Krishanu = Employee("Krishanu Karmakar", 545541, 23)
Krishanu.printDetails()

Krishanu.Function_of_class_Employee()
Employee.Function_of_class_Employee()