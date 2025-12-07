import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)


# polymorphism_demo.py doesn't 
# contain: ["self.length", "self.length * self.width"]