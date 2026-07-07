### Q1.
# Create a second Student object with a different name and make it say hello.

class Student:  # class
    name = 'Swaham'
    def say_hello(self):
        print(f"Hello, my name is {self.name}.")
    
S = Student()   # object
print(S.name)
        
S1 = Student()  # second object
S1.say_hello()