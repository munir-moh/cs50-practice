# ============================
# Lecture 0 – Python Basics
# ============================

# 1. Creating Code with Python
print("Hello, World!")  # Basic print statement


# 2. Functions
def greet(name):
    # A function that greets a user by name
    print("Hello, " + name + "!")

greet("Aisha")
greet("Munir")


# 3. Bugs
# Example of a bug (TypeError: can't add str and int)
# print("The sum is: " + 5 + 3)   # ❌ Uncommenting will cause error

# Corrected version
print("The sum is:", 5 + 3)


# 4. Improving Your First Python Program
# (a) Variables
name = "Aisha"
age = 20
print(name, "is", age, "years old.")

# (b) Comments
# Single-line comment example
"""
This is a multi-line comment
explaining more details about the code
"""
print("Comments are ignored by Python")

# (c) Pseudocode example:
# Pseudocode:
# 1. Ask user for two numbers
# 2. Add them
# 3. Print result

# Actual code:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Sum:", a + b)


# 5. Further Improving Your First Python Program
def add_numbers():
    """Function that safely adds two numbers from user input"""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Sum is:", a + b)
    except ValueError:
        print("Invalid input, please enter numbers only!")

# Uncomment to test
# add_numbers()


# 6. Strings and Parameters
def greet_user(name):
    print("Welcome,", name)

greet_user("Munir")

# Small problem with quotation marks
print("She said, 'Python is fun!'")
print('He replied, "Yes, it is!"')


# 7. Formatting Strings
name = "Aisha"
age = 20

# Using f-string
print(f"{name} is {age} years old.")

# Using format method
print("{} is {} years old.".format(name, age))


# 8. More on Strings
s = "  Python Programming  "
print(s.lower())      # Convert to lowercase
print(s.upper())      # Convert to uppercase
print(s.strip())      # Remove surrounding spaces
print(s.replace("Python", "Java"))  # Replace words
print(s[0:6])         # Slicing: prints "Python"


# 9. Integers or int
x = 10
y = 3
print(x + y)   # Addition
print(x - y)   # Subtraction
print(x * y)   # Multiplication
print(x // y)  # Floor division
print(x % y)   # Modulus
print(x ** y)  # Power


# 10. Readability Wins
# Bad example (hard to read):
print(((5*5)+(10/2)))

# Good example (clearer):
square = 5 * 5
half = 10 / 2
result = square + half
print(result)


# 11. Float Basics
pi = 3.14159
radius = 2.5
area = pi * radius ** 2
print("Circle area:", area)


# 12. More on Floats
x = 0.1 + 0.2
print(x)  # Floating-point precision issue

# Rounding to 2 decimal places
print(round(x, 2))


# 13. Def
# "def" keyword is used to define functions
def multiply(a, b):
    return a * b

print(multiply(4, 5))


# 14. Returning Values
def square(x):
    return x * x

result = square(6)
print("Square is:", result)


# 15. Summing Up – Calculator Example
def calculator(a, b):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

calculator(10, 5)