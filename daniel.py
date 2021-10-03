import random


random_number = random.randint(1, 100)


print('''

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Guess the randomized number, it's between 1-100.
You have 10 tries.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

''')

guesses = [1]
points = 1000
tries = 10
guess = int(input("Guess a number: "))


while random_number != "guess" and tries > 0:
    if guess > random_number:
        tries -= 1
        print(f"The randomized number is lower and you have <{tries}> tries left")
        guess = int(input("Guess again: "))
        guesses.append(1)

    elif guess < random_number:
        tries -= 1
        print(f"The randomized number is higher and you have <{tries}> tries left")
        guess = int(input("Guess again: "))
        guesses.append(1)

    elif guess == random_number:
        print(f"You have won {points * (10 - len(guesses))} points by guessing the right number")
        break
