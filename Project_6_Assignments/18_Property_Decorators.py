# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

# Hint: Use the @ decorator to mark the method as a property.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

product = Product(10)
print(product.price)  # Output: 10

product.price = 20
print(product.price)  # Output: 20

del product.price

# Output:
# 10
# 20
#