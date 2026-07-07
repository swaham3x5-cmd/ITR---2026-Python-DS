class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def showSalary(self):
        print("Emp salary = ", self.__salary)
        
emp = Employees(input("Enter Name = "),input("Enter Salary = "))
print(emp.name)
emp.showSalary()
# print(emp.__salary)d