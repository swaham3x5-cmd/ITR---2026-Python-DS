### Q2.
class Animal:
    def speak(self):
        print("Animal")
# Create a class Bird that inherits from Animal.
class Bird(Animal):
    # Override the speak() method to print:
    def speak(self):
        print("Tweet!") # Tweet!
    
# Create a Bird object and call the speak() method.
obj = Bird()
obj.speak()