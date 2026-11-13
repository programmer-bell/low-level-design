## Abstraction 

'''
Abstraction is about reducing complexity. You expose only the necessary details to the user and 
hide all the complicated internal logic. The user does not need to know how things work inside
just that they work.

'''
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# s = Shape()
# s.area()

class Rectangle(Shape):
    def __init__(self, length: int, breadth: int):
        self.lenght: int = length
        self.breadth : int = breadth

    def area(self):
        print(self.lenght * self.breadth)

    def perimeter(self):
        print(2 * (self.lenght + self.breadth))

r = Rectangle(5, 2)
r.area()
r.perimeter()