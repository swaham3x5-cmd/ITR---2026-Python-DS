# Create an "Employee" class with a private "__salary" attribute and methods to update and display the salary.

class Employee:
    def __init__(self, Salary):
        self.__Salary = Salary
    
    def update_Salary(self, new_salary):
        self.__Salary = new_salary
    def display_Salary(self):
        print(f"Salary: {self.__Salary}")
        
S1 = Employee(85000)

print("Before updating salary:")
S1.display_Salary()

print("After updating salary:")
S1.update_Salary(90000)
S1.display_Salary()