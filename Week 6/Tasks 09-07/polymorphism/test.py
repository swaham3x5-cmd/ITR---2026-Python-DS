# Q3
class Person:
    def __init__(self):
        print("This is person!")

class Teacher(Person):
    def __init__(self):
        print("This is teacher inheriting person...")

# Object Initialization and function calling.
t = Teacher()
t.__init__()