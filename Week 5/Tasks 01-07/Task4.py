### Q4.
# Create another Student object with different details and display its information.

class Student:  # class
    name =''
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
S1 = Student("Swaham", 18)
S1.show_info()

S2 = Student("Radha", 19)
S2.show_info()