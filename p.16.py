import random
a=random.randint(10,50)
b=0
while b<5:
    guess=int(input("Guess the number between 10 to 50:\n"))
    if guess==a:
        print("You win")
        break
    else:
        b+=1
    if not b<5:
        print("you lose:(\n THe number was",a)
