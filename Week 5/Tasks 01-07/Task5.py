### Q5.
# Create a class Bike with a class variable wheels = 2 and an instance variable color
# similar to the Car class. 
# Instantiate a Bike object and print its color and wheels.

class Bike:
    wheels = 2  # class variable
    def __init__(self,color):
        self.color = color  # instance variable

Bike1 = Bike("red")
Bike2 = Bike("blue")

print(f"Color of bikes {Bike1.color} and {Bike2.color}")
print(f"Wheels of bikes {Bike.wheels}")