# Write a function that takes a list of numbers and returns the sum of those numbers.

# Here's a sample run of the program (user input is in bold italics):
def add_numbers(numbers)-> int:
    total:int = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    sum_of_numbers: int = add_numbers(numbers)
    print("The sum of", numbers, "is", sum_of_numbers)

if __name__ == '__main__':
    main()