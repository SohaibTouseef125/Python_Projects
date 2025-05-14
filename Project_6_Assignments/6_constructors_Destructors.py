# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self, message):
        print(message)

    def __del__(self):
        print("Object destroyed")

logger = Logger("Object created")
del logger

# Output:
# Object created
# Object destroyed