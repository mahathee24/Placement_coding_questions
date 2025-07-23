class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

# Taking user input
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Creating object
rect = Rectangle(length, breadth)

# Calculating and displaying area
area = rect.calculate_area()
print(f"The area of the rectangle is: {area}")






