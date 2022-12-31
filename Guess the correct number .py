import random
while True:
    a = random.randint(1, 1000)
    b = int(input("Guess number between 1 and 1000 \n"))
    if a == b:
        print("You guessed it right")
    else:
        print("You guessed it wrong. Better luck next time")
    c = input("Do you want to continue? (Y/N) ")
    if c.upper() == "Y":
        continue
    else:
        break
