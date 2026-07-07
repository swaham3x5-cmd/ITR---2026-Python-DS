### Q3.
# Modify the Student class so that the __init__() method also accepts an age parameter and stores it.
# Update the show_info() method to display the student's age.

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