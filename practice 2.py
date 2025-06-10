# Create a class Rectangle with attributes width and height.
# Add a method area() that returns the area (width × height).

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5,3)
print("Area of rectangle:", rect.area())