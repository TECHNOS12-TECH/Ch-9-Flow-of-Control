a=int(input("Enter hours between 1 to 12: "))
b=int(input("How many hours ahead: "))
if a+b>12:
    print("Time at that time would be",(a+b)-12,"O'clock")
else:
    print("Time at that time would be",a+b,"O'clock")
    
