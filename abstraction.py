from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def get_color(self):
        return self.color

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Using the classes
rect = Rectangle("blue", 10, 5)
print("Rectangle area:", rect.area())
print("Rectangle perimeter:", rect.perimeter())
print("Rectangle color:", rect.get_color())

circle = Circle("red", 7)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())
print("Circle color:", circle.get_color())
