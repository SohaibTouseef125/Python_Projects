import random
def guess_number_computer():
    print("Welcome to guess the number game computer")
    low = 1
    high = 10
    print(f"Please think of a number between {low} and {high}")
    if low <= high:
        guess = random.randint(low, high)
        print(f"Computer's guess is {guess}")
        while True:
            response = input(f"Is the guess {guess} too high, (H), too low (L), or correct (C) too low, or correct? ").lower()
            if response == "C":
                print("Yay! The computer guessed the number!")
                break
            elif response == "H":
                high = guess - 1
                guess = random.randint(low, high)
                print(f"Computer guessed the number {guess}")
            elif response == "L":
                low = guess + 1
                guess = random.randint(low, high)
                print(f"Computer guessed the number {guess}")
            else:
                print("Invalid response. Please try again.")
                if low > high:
                    print("The computer could not guess the number. Please try again.")             
          
if __name__ == "__main__":
    guess_number_computer()
