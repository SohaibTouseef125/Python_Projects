import random
print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 10)
print("I'm thinking of a number between 1 and 10.")
while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Congratulations! You guessed the number!", secret_number)
            break
    except ValueError:
        print("Invalid input. Please enter a number.")


