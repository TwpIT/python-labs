import math

#1
degree = input("Input degree: ")
print("Output radian:", math.radians(float(degree)))

#2
def trapezoid(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
print("Expected Output:", trapezoid(height, base1, base2))

#3
def regular_polygon_area(sides, length):
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
print("The area of the polygon is:", regular_polygon_area(sides, length))

#4
def parallelogram_area(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
print("Expected Output:", parallelogram_area(base, height))
