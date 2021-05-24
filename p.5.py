a=float(input("Enter 1st multiple: "))
b=float(input("Enter 2nd multiple: "))
c=float(input("Enter 3rd multiple: "))
d=float(input("Enter 4th multiple: "))
e=float(input("Enter 5th multiple: "))
div=float(input("Enter value of divisor: "))
count=0
if a%div==0:
    count+=1
if b%div==0:
    count+=1
if c%div==0:
    count+=1
if d%div==0:
    count+=1
if e%div==0:
    count+=1
print("Number of multiples of divisor from the given number:",count)
