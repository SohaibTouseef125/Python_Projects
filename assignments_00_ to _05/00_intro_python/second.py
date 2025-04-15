# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!

# Ask the user for their favorite animal
def main():
    animal = input("\033[1;3m What's your favorite animal?\033[0m ")

# Respond with the same animal
    print(f"My favorite animal is also {animal}!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
