def circle_area(radius):
    return 3.14 * radius * radius

def square_area(side):
    return side * side

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, breadth):
    return length * breadth

while True:
    print("\nChoose a shape to calculate area:")
    print("circle")
    print("square")
    print("triangle")
    print("rectangle")

    shape = input("Enter the shape name: ").lower()


    match shape:
        case "circle":
            radius = float(input("Enter the radius: "))
            print("Area of circle:", circle_area(radius))

        case "square":
            side = float(input("Enter the side: "))
            print("Area of square:", square_area(side))

        case "triangle":
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            print("Area of triangle:", triangle_area(base, height))

        case "rectangle":
            length = float(input("Enter the length: "))
            breadth = float(input("Enter the breadth: "))
            print("Area of rectangle:", rectangle_area(length, breadth))

        case _:
            print("Invalid shape. Please try again.")
