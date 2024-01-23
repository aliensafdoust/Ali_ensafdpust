import random
import sys

while True:
    try:
        number = int(input("Level: "))
        if number >= 0:
            random = random.randint(1, number)
            break
    except ValueError:
        print("try again !!")
        pass

while True:
    try:
        guees = int(input("Guess: "))
        if guees < random:
            print("Too small!")
        elif guees > random:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit(0)
    except ValueError:
        print("try again !!")
        pass
