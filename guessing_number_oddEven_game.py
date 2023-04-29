import random

number = random.randint(199, 100000)
number_of_guessing = 0

while number_of_guessing < 20:
    print(number)
    print("Is that number even?")
    guess = input()

    if number % 2 == 0 and guess == "yes" or guess == "Yes":
        print("You're right! ", number, " is an even number")
        break
    elif number % 2 == 0 and guess == "no" or guess == "No":
        print("You're wrong! ", number, " is an even number")
        break
    elif number % 2 != 0 and guess == "no" or guess == "No":
        print("You're wrong! ", number, " is an odd number")
        break
    elif number % 2 != 0 and guess == "yes" or guess == "Yes":
        print("You're right! ", number, " is an odd number")
        break
    elif number_of_guessing == 20:
        print("You're ran out of guesses")
        break
else:
    print("please try again")
