a=int(input("Enter a number "))
maxi,mini=a,a
for i in range(0,4):
    a=int(input("Enter a number "))
    if maxi<a:
        maxi=a
    if mini>a:
        mini=a
print("Maximum number you have entered is: ",maxi)
print("Minimum number you have entered is: ",mini)
