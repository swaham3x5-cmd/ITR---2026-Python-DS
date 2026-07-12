# Parent Class 
class Parent:
    def myMethod(self):
        print("This is parent class.")

# Child Class        
class Child(Parent):
    def myMethod(self):
        print("This is Parent Class method in Child Class(Overridden)")

# Instance of child

c = Child()

c.myMethod()