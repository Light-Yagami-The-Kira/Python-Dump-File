class Programmer:
    salary = 5000
    bonus = 500
    
    @property
    def totalSalary(self):
        return self.salary + self.bonus
    
    @totalSalary.setter
    def totalSalary(self,totalSalary):
        self.bonus = totalSalary - self.salary
    
Krishanu = Programmer()
# Krishanu.bonus = 600
print(Krishanu.totalSalary)

Krishanu.totalSalary = 10000

print(Krishanu.totalSalary, Krishanu.salary, Krishanu.bonus)

