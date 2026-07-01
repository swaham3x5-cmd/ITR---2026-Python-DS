class Car:
    wheels = 4  # class variable
    def __init__(self,color):
        self.color = color  # instance variable

car1 = Car("red")
car2 = Car("blue")

print(f"{car1.color} and {car2.color}")
print(f"{Car.wheels}")