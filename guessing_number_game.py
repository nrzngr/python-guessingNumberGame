import random

number = random.randint(1, 50)
number_of_guessing = 0

while number_of_guessing <= 10:
    print("Guess a number between 1 and 50: ")
    guess = int(input())
    number_of_guessing += 1

    if guess == number:
        print("Congrats, You right! the number is ",
              number, " you did it in ", number_of_guessing)
        break
    elif number_of_guessing == 10:
        print("Sorry, you did not guess the number. The number was " + number)
        break
    elif guess > 50:
        print("You are out of guessing range, please try again")
        break
else:
    print("Sorry, You didn't guess it right")
