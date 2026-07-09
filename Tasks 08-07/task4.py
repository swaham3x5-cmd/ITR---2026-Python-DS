# Q4
class Flyer:
    def fly(self):
        print("Flying high!")

class Swimmer:
    def swim(self):
        print("Swimming deep!")

class FlyingFish(Flyer, Swimmer):
    pass  # Inherits from both

# Object Initialization and function calling.
f = FlyingFish()
f.fly()
f.swim()