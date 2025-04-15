# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    feet: int = int(input("Enter number of feet: "))
    print("There are", feet * 12, "inches in", feet, "feet.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()