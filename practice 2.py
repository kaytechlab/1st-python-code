# Create a class Rectangle with attributes width and height.
# Add a method area() that returns the area (width × height).

print(0/1)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5,3)
print("Area of rectangle:", rect.area())

val = 100000000000000
while True:
    try:
        div = int(input(f"{val} divided by:"))
        val /= div
    except ValueError:
        print("Don;t make foolish mistazks agkizn: ")

    except ZeroDivisionError:
        print("000000 zero what are u smokin ")
    finally:
        print("calc done")
