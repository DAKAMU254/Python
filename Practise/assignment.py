# Area of a triangle
# Function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

# Input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate and display the area
area = triangle_area(base, height)
print(f"The area of the triangle is: {area}")


# Area of a circle
import math

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius**2

# Input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the area
area = circle_area(radius)
print(f"The area of the circle is: {area}")



# Area of a rectangle
# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and display the area
area = rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")
