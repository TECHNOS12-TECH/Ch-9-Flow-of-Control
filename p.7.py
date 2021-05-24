import math
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
oper=input("Choose your operators[+,-,*,/,%]:")
if oper=="+":
    print("Result=",a+b)
elif oper=="-":
    print("Result=",a-b)
elif oper=="*":
    print("Result=",a*b)
elif oper=="/":
    print("Result=",a/b)
elif oper=="%":
    print("Result=",a%b)
else:
    print("You have used invalid operator")
