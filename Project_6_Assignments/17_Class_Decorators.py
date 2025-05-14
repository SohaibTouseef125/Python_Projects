# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# Hint: Use the @ decorator to mark the class as a decorator.

class add_greeting:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        self.cls.greet = lambda: "Hello from Decorator!"
        return self.cls

@add_greeting
class Person:
    pass

person = Person()
print(person.greet())

# Output:
# Hello from Decorator!