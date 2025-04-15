# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def main(lst):
    """
    Prints the last element of a provided list.
    """
    print(lst[len(lst)-1])

    # This provided line is required at the end of a Python file
    # to call the main() function.
if __name__ == '__main__':
    main()