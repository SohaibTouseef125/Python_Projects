# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

# Hint: Use the @staticmethod decorator to mark the method as a static method.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

temp = TemperatureConverter.celsius_to_fahrenheit(25)
print(temp)