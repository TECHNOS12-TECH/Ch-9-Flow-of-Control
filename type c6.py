a=float(input("Enter 1st side: "))
b=float(input("Enter 2nd side: "))
c=float(input("Enter 3rd side: "))
if a+b>c and a+c>b and b+c>a:
    print("Yes it is a triangle with sides",a,b,c)
else:
    print("It is not a triangle")
