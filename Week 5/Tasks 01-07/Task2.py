### Q2.
# Add an age attribute using a method (e.g., set_age()), and modify say_hello() to include the student's age.

class Student:  # class
    name = 'Swaham'
    age = None

    def set_age(self, age):
        self.age = age

    def disp_age(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
S1 = Student()

S1.set_age(18)
S1.disp_age()