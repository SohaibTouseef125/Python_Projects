# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# This provided line is required at the end of a Python file
# to call the main() function.
def main():
    numbers = [1, 2, 3, 4]
    for i in range(len(numbers)):
        numbers[i] *= 2
    print(numbers)


if __name__ == '__main__':
    main()