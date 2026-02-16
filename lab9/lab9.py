# Lab 9
# Error Handling and Debugging

print("=== 1) Exceptions ===")
try:
    x = 0
    print(10 / x)
except ZeroDivisionError as e:
    print("Caught:", e)

print("\n=== 2) Common Built-in Exceptions ===")

# ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# ValueError
try:
    x = int("abc")
except ValueError as e:
    print("ValueError:", e)

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("IndexError:", e)

# KeyError
try:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_dict['k'])
except KeyError as e:
    print("KeyError:", e)

# TypeError
try:
    print("2" + 2)
except TypeError as e:
    print("TypeError:", e)

# FileNotFoundError
try:
    open("non_exist_file.txt")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

print("\n=== 3) try/except with user input ===")
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please enter valid integer number")

print("\n=== 4) Handling Multiple Exceptions ===")
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except (ZeroDivisionError, ValueError):
    print("Error: Invalid operation.")

print("\n=== 5) else in Exception Handling ===")
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please enter valid integer number")
else:
    print("Result:", result)

print("\n=== 6) finally ===")
file = None
try:
    file = open("example.txt", "r")
    content = file.read()
    print("File content read successfully.")
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")
    if file is not None:
        file.close()

print("\n=== 7) Raising Exceptions ===")

def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Amount can't be greater than balance")
    return balance - amount

try:
    new_balance = withdraw(200, 100)
    print("New balance:", new_balance)
except ValueError as e:
    print(f"Error: {e}")

class Shape:
    def area(self):
        raise NotImplementedError("You must implement this method")

print("\n=== 8) Custom Exceptions ===")

class NegativeNumberException(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        super().__init__(message)

def square_root(x):
    if x < 0:
        raise NegativeNumberException("Cannot compute the square root of negative number")
    return x ** 0.5

try:
    result = square_root(-5)
    print(result)
except NegativeNumberException as e:
    print(f"Error: {e}")

print("\n=== 9) Debugging in Python ===")

# Using Print Statements
def add(a, b):
    print(f"a: {a}, b: {b}")
    return a + b

print("add result:", add(1, 2))

# Using Assertions
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

try:
    print("divide result:", divide(10, 0))
except AssertionError as e:
    print("AssertionError:", e)
