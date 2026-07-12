# Q3
class Person:
    def greet(self):
        print("Hello!")

class Teacher(Person):
    def teach(self):
        print("Teaching...")

# Object Initialization and function calling.
t = Teacher()
t.greet()   # Inherited
t.teach()   # Own method