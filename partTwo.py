import random
userguess = 0

guessingnumber = random.randint(1,10)

while (userguess != guessingnumber):
    userguess = int(input("Guess a number between 1 and 10."))
    if (userguess > 10 or userguess <= 0):
        print("Invalid guess.")
    elif (userguess > guessingnumber):
        print("Too high.")
    elif (userguess < guessingnumber):
        print("Too low.")
    else:
        print("Correct.")

