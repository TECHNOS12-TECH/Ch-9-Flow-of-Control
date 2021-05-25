print("For Quadratic equation of general form ax^2+bx+c=0")
print("Enter values of a,b and c")
import math
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
c=float(input("Enter value of c: "))
d=b**2-4*a*c
x1=0
x2=0
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("Roots of quadractic equation are (Real and distinct)",x1,x2)
elif d==0:
    x1=(-b)/2*a
    print("Roots of quadractic equation are (Real and equal)",x1,x1)
else:
    print("Roots are complex/Imaginary(As D<0)")
