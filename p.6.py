import math
radius=float(input("Enter value of radius: "))
print("1 is choice for Area")
print("2 is choice for Perimetre")
choice=int(input("What is your choice(1 or 2)? "))
if choice==1:
    print("The Area of a circle is:",math.pi*radius**2)
else:
    print("The Perimetre of a circle is:",2*math.pi*radius)
