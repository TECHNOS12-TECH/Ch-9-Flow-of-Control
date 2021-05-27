# Prime or not
a=int(input("Enter you want to check: "))
b=False
if a>1:
    for i in range(2,a):
        if a%i==0:
            b=True

if b:
    print(a,"is not prime")
else:
    print(a,"is prime")
