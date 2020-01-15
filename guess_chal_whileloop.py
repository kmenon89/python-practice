#make user guess random numbers 
#give hints if they need to guess higher or lower

import random

highest=10
answer=random.randint(1,highest)

guess=input("please guess a number between 1 and {0} (type 0 to quit the game):".format(highest))

if guess:

    while answer!=int(guess):
        if int(guess)>answer:
            print("please guess lower:")
        elif int(guess)==0:
            print("you have quit the game!")
            break
        else :
            print("Please guess higher:")
        guess=input("please guess a number between 1 and {0} (type 0 to quit the game):".format(highest))

    else:
        print("you have guessed right!")
else :
    print("please guess a valid numer!")