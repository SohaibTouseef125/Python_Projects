# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

# Hint: Use the __call__() method to mark the class as callable.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return self.factor * x

    def multiply(self, x):
        return self.factor * x

    def __repr__(self):
        return f"Multiplier({self.factor})"

m = Multiplier(3)
print(callable(m))  # Output: True

print(m(5))  # Output: 15   

print(m.multiply(5))  # Output: 15

print(m)

# Output:
# Multiplier(3)
