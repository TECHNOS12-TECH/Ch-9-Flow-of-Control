a = int(input("ENTER NUMBER "))
maxi,mini=a,a
for i in range(0,4):
    a = int(input("ENTER NUMBER "))
    if maxi<a:
        maxi = a
    if mini>a:
        mini = a
print("The maximum value of 5 numbers is:",maxi)
print("The minimum value of 5 numbers is:",mini)
