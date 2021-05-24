items=int(input("Enter total number of items:"))
if items<10:
    print("Your total cost of items is:",items*120,"Rs")
elif 10<items<99:
    print("Your total cost of items is:",items*100,"Rs")
elif items>=100:
    print("Your total cost of items is:",items*70,"Rs")
