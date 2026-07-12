### Q1.
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

# Create a class Circle that inherits from Shape.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement the area() method to return:
    def area(self):
        return 3.14 * self.radius * self.radius

# Instantiate a Circle object with *radius = 3* and print its area.
obj = Circle(3)
print(f"Area of Circle = {obj.area()}")