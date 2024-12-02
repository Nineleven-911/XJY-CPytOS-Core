import random

targ = random.randint(1, 100)
while 1:
    guess = int(input(" >"))
    if guess > targ:
        print("Bigger!")
    elif guess < targ:
        print("Smaller!")
    else:
        print("You guess it!")
        break
