class Employee:
    def __init__(self, name, age):
        self.name = name
        self._age = age
class subEmployee(Employee):
    def showAge(self):
        print("Age:",self._age)
        
emp = subEmployee("Swaham",18)
print(emp.name)
emp.showAge()