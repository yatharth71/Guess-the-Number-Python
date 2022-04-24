import random

number = random.randint(0, 100)

notGuessed = True

askedTime = 0

while notGuessed:
    askedTime += 1

    print("The number is between 0 to 100")
    guess = int(input("Enter your guess : "))

    if guess > number:
        if (guess - number) >= 20:
            print("Too High")
        elif (guess - number) <= 10:
            print("Near")
        elif (guess - number) <= 5:
            print("Very Near")
        else:
            print("Sorry but i cannot understand")

    elif guess < number:
        if (number - guess) >= 20:
            print("Too Low")
        elif (number - guess) <= 10:
            print("Near")
        elif (number - guess) <= 5:
            print("Very Near")
        else:
            print("Sorry but i cannot understand")

    elif guess == number:
        print(f"Correct Guess, the number was {number}")
        notGuessed = False

    if askedTime > 5:
        print(f"The number was {number}")
        break
