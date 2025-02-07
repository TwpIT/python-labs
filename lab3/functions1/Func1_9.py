import math
def s_of_sphere(radius):
    return (4/3) * (math.pi) * (radius ** 3)

def s_of_sphere_with_pi(radius):
    return str((4/3) * (radius ** 3)) + "π"
print(s_of_sphere_with_pi(int(input("put radius: "))))
