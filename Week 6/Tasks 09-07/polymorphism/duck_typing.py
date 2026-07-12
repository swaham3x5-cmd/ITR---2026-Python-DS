class Duck:
    def sound(self):
        print("quack")

class AnotherBird:
    def sound(self):
        print("Bird similar to duck")
     
def makeSound(bird):
    bird.sound()

# Creating Instances
duck = Duck()
anotherBird = AnotherBird()

# Calling Methods
makeSound(duck)
makeSound(anotherBird)