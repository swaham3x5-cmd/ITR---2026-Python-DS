class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self,name, age,roll_no):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No.: {self.roll_no}")
        
obj = Student("Swaham", 18, 45)
obj.show()