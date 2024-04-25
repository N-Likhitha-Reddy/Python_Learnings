
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of rectangle is ", self.length * self.width)

    def perimeter(self):
        print("Perimeter of rectangle is ", (2 * (self.length + self.width)))


n = int(input("Enter number of rectangles for which you want to find area and perimeter: "))
for i in range(n):
    length = int(input(f"Enter length of rectangle{i+1} "))
    width = int(input(f"Enter width of rectangle{i+1} "))
    rectangle = Rectangle(length, width)
    rectangle.area()
    rectangle.perimeter()

