class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rect = Rectangle(length, width)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")