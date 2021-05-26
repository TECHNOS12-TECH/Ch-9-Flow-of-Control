n=int(input("Enter number natural number upto which you want to print sum:\n"))
sum1=0
sum2=0
a=1
while a<=n:
    if a%2==0:
        sum1+=a
    else:
        sum2+=a
    a+=1
print("Sum of even natural number >=",n,"is",sum1)
print("Sum of odd natural number >=",n,"is",sum2)
