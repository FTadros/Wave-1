from math import pi
radius = input("Please input the radius of the cylinder: ")
height = input("Please input the height of the cylinder: ")

radius = int(radius)
height = int(height)

volume = pi * (radius ** 2) * height
volume = round(volume, 1)
print("The volume of your cylinder is ", volume)
