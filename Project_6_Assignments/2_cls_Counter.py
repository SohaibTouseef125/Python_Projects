# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

    def __init__(self):
        Counter.count += 1

    def __del__(self):
        Counter.count -= 1

counter1 = Counter()
counter2 = Counter()
counter3 = Counter()


Counter.display_count()

del counter1
del counter2
del counter3

Counter.display_count()

# Output:
# Total objects created: 3
# Total objects created: 0
