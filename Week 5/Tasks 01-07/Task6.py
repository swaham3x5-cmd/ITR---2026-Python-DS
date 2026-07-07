### Q6.
# Create a new Car object (e.g., car3 = Car("green")) and print car3.color and Car.wheels.

class Car:
    wheels = 4  # class variable
    def __init__(self,color):
        self.color = color  # instance variable

car1 = Car("red")
car2 = Car("blue")

print(f"{car1.color} and {car2.color}")
print(f"{Car.wheels}")

car3 = Car("green")
print(f"{car3.color} and {Car.wheels}")