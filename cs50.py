# Lecture 0 – Python Basics


# 1. Creating Code with Python
print("Hello, World!")  


# 2. Functions
# In python, there are built-in functions like print(), input(), len(), etc.


# 3. Improving Your First Python Program
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


# 4. Strings and Parameters
def greet_user(name):
    print("Welcome,", name)

greet_user("Munir")

# Small problem with quotation marks
print("She said, 'Python is fun!'")
print('He replied, "Yes, it is!"')


# 5. Formatting Strings
name = "Aisha"
age = 20

# Using f-string
print(f"{name} is {age} years old.")

# Using format method
print("{} is {} years old.".format(name, age))


# 6. More on Strings
s = "Python Programming"
print(s.lower())      # Convert to lowercase
print(s.upper())      # Convert to uppercase
print(s.strip())      # Remove surrounding spaces
print(s.replace("Python", "Java"))  # Replace words
print(s[0:6])         # Slicing: prints "Python"


# 7. Integers or int
x = 10
y = 3
print(x + y)   # Addition
print(x - y)   # Subtraction
print(x * y)   # Multiplication
print(x // y)  # Floor division
print(x % y)   # Modulus
print(x ** y)  # Power


# 8. Readability Wins
# Bad example (hard to read):
print(((5*5)+(10/2)))

# Good example (clearer):
square = 5 * 5
half = 10 / 2
result = square + half
print(result)


# 9. Float Basics
pi = 3.14159
radius = 2.5
area = pi * radius ** 2
print("Circle area:", area)


# 10. More on Floats
x = 0.1 + 0.2
print(x)  # Floating-point precision issue

# Rounding to 2 decimal places
print(round(x, 2))


# 11. Def
# "def" keyword is used to define functions
def multiply(a, b):
    return a * b

print(multiply(4, 5))


# 12. Returning Values
def square(x):
    return x * x

result = square(6)
print("Square is:", result)

