a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
sum1=a+b+c
sum2=0
if a!=b and a!=c:
    sum2+=a
if b!=a and b!=c:
    sum2+=b
if c!=a and c!=b:
    sum2+=c
print("Numbers are",a,b,c)
print("The sum of all numbers:",sum1)
print("The sum of all non-dublicate numbers:",sum2)
