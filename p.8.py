a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
c=float(input("Enter 3rd number: "))
if a>b and a>c:
    if b>c:
        maxi,mid,mini=a,b,c
    else:
        maxi,mid,mini=a,c,b
elif b>a and b>c:
    if a>c:
        maxi,mid,mini=b,a,c
    else:
        maxi,mid,mini=b,c,a
else:
    if a>b:
        maxi,mid,mini=c,a,b
    else:
        maxi,mid,mini=c,b,a 
print("The numbers in Descending order:",maxi,mid,mini)
