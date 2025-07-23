class rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def set_dim(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        print("Area:", self.a * self.b)

nums = []
d = int(input("Enter number of rectangles: "))

for i in range(d):
    R = rect(i+10,i+20)
    a = int(input(f"Enter length of rectangle {i+1}: "))
    b = int(input(f"Enter breadth of rectangle {i+1}: "))
    R.set_dim(a, b)
    nums.append(R)

print("\nAreas of rectangles:")
for i in range(d):
    print(f"Rectangle {i+1}: ", end='')
    nums[i].area() 