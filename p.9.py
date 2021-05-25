char=input("Enter your character: ")
if char>="A" and char<="Z":
    print("Your character is an Uppercase")
elif char>="a" and char<="z":
    print("Your character is an Lowercase")
elif char>="0" and char<="9":
    print("Your character is a digit")
else:
    print("You have entered special Character")
