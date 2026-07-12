class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no

class Employee(Person):
    def __init__(self, name, emp_id):
        Person.__init__(self, name)      
        self.emp_id = emp_id

class Teaching_Assistant(Student, Employee):
    def __init__(self, name, roll_no, emp_id):
        Student.__init__(self, name, roll_no)
        Employee.__init__(self, name, emp_id)
    
    def show(self):
        print(f"Name: {self.name}, Roll No.: {self.roll_no}, EMP_ID: {self.emp_id}")

S = Teaching_Assistant("Swaham", 45, 123456789)
S.show()