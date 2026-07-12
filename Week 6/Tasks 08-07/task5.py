# Q5
class Manager:
    def greet(self):
        print("Hello, I am a Manager.")

class Director(Manager):
    def greet(self):
        print("Hello, I am a Manager (Director).")  # Overridden

# Object Initialization and function calling.
d = Director()
d.greet()