class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgramer(Player, Employee):

    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan",["Cricket"])
det = karan.printdetails()
karan.printlanguage()
print(det)
print(karan.var)

# ========================================================================================

class Base1:
    def __init__(self):
        print("Base1 constructor")

class Base2:
    def __init__(self):
        print("Base2 constructor")

class Derived(Base1, Base2):
    def __init__(self):
        super().__init__()  # Calls the constructor of the leftmost base class (Base1)
        Base2.__init__(self)  # Calls the constructor of the second base class (Base2)
        print("Derived constructor")
    pass

# Create an instance of the derived class
obj = Derived()
