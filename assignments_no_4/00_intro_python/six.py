# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0
def main():
    num = float(input("\033[1;3m Type a number to see its square: \033[0m"))
    print(f"{num} squared is {num*num}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()