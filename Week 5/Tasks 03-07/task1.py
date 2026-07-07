# Write a Python program to create a "Student" class with a private "__marks" attribute and a method to display marks.

class Student:
    def __init__(self, marks):
        self.__marks = marks
    
    def display_marks(self):
        print(f"Marks: {self.__marks}")
        
S1 = Student(85)
S1.display_marks()