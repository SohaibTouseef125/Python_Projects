# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()


# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

# Hint: the number of seconds in a year is 365 * 24 * 60 * 60
Days = 365
Hours = 24
Minutes = 60
Seconds = 60
def main():
    print("There are" + str(Days * Hours * Minutes * Seconds) + "seconds in a year!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()