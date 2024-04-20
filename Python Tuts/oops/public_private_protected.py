class Employee:
    public = 1
    _protected = 2
    __private = 3

a = Employee()

print(a.public)
print(a._protected)
# print(a.__private)
print(a._Employee__private)


class Boss:

    @staticmethod
    def getEmployeeData(emp):
        print(emp.public)
        print(emp._protected)
        # print(emp.__private)

Boss.getEmployeeData(a)