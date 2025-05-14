# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# Hint: Use the __init__() method to pass a reference to the Employee object to the Department class.

class Department:
    def __init__(self, employee):
        self.employee = employee

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee = Employee("Sohaib", 50000)
department = Department(employee)

print(department.employee.name)
print(department.employee.salary)

