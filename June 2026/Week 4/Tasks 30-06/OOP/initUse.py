class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showAge(self):
        print(f"Hello! I'm a Person named {self.name},{self.age} years old.")
        
Person1 = Person("Swaham",18)
Person1.showAge()

Person2 = Person("Priya",23)
Person2.showAge()