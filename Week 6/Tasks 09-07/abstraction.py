from abc import ABC, abstractmethod     # abc = Abstract Base Class

class Shape:
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side

S1 = Square(10)
print(S1.area())