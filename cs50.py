# LECTURE 0 – Python Basics


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



#LECTURE 1
# 1. Conditionals
"""Conditionals allow you, the programmer, to allow your program to make decisions: As if your program has the choice between taking the left-hand road or the right-hand road based upon certain conditions.
Conditionals allow your program to make decisions, choosing one path over another depending on specified conditions.
Built within Python are a set of “operators” that are used to ask mathematical questions.
> and < symbols are probably quite familiar to you.
>= denotes “greater than or equal to.”
<= denotes “less than or equal to.”
== denotes “equals.” Note the double equal sign: a single equal sign assigns a value, whereas two equal signs compare values.
!= denotes “not equal to.”
Conditional statements compare a left-hand term to a right-hand term."""

#if Statements
#if statements use bool (Boolean) values (True or False) to decide whether or not to execute code. If the comparison x > y is True, the interpreter runs the indented block.

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

#Control Flow, elif, and else
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# 'or' allows your program to decide between one or more alternatives. For example, 
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# 'and' Similar to or, and can be used within conditional statements. For example,
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >=70 and score < 80:
    print("Grade: C")
elif score >=60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# Modulus
#The modulo % operator in programming allows one to see if two numbers divide evenly or divide and have a remainder. For example, 10 % 3 is 1 because 10 divided by 3 is 3 with a remainder of 1.
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#Creating Our Own Parity Function
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

#Pythonic
#In the programming world, there are types of programming that are called “Pythonic” in nature. That is, there are ways to program that are sometimes only seen in Python programming

#match
"""Similar to if, elif, and else statements, match statements can be used to conditionally run code that matches certain values.
Consider the following program:
"""

name = input("What's your name? ")

if name == "Harry":
  print("Gryffindor")
elif name == "Hermione":
  print("Gryffindor")
elif name == "Ron": 
  print("Gryffindor")
elif name == "Draco":
  print("Slytherin")
else:
  print("Who?")
#Notice the first three conditional statements print the same response.

#We can improve this code slightly with the use of the or keyword:
  name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron": 
  print("Gryffindor")
elif name == "Draco":
  print("Slytherin")
else:
  print("Who?")
#Notice the number of elif statements has decreased, improving the readability of our code.

#Alternatively, we can use match statements to map names to houses. Consider the following code:
  name = input("What's your name? ")

  match name: 
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron": 
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
#Notice the use of the _ symbol in the last case. This will match with any input, resulting in similar behavior as an else statement.

"""A match statement compares the value following the match keyword with each of the values following the case keywords. In the event a match is found, the respective indented code section is executed, and the program stops the matching.
We can improve the code:
"""
  name = input("What's your name? ")

  match name: 
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
#Notice, the use of the single vertical bar |. Much like the or keyword, this allows us to check for multiple values in the same case statement.

#LECTURE 2

# 1. WHILE LOOP
# A while loop keeps running as long as its condition is True.

count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # increase count so the loop eventually ends


# 2. FOR LOOP
# A for loop is used to iterate over a sequence (like a list, string, or range).

for i in range(1, 6):
    print("Number:", i)



# 3. CONTINUE
# 'continue' skips the current iteration and moves to the next.

for num in range(1, 6):
    if num == 3:
        continue 
    print(num)


# 4. BREAK
# 'break' stops the loop completely.

for num in range(1, 6):
    if num == 4:
        break  
    print(num)


# 5. PASS
# 'pass' does nothing. It is used as a placeholder.

for num in range(1, 6):
    if num == 3:
        pass  
    print("Number:", num)




# 6. LISTS
# A list is a collection of items in a particular order.

fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing items
print(fruits[0])  
print(fruits[1])   
# Adding items
fruits.append("orange")
print(fruits)  

# Removing items
fruits.remove("banana")
print(fruits) 


# 7. LENGTH

numbers = [10, 20, 30, 40, 50]
print("Length of numbers list:", len(numbers)) 


# 8. DICTIONARIES
# A dictionary is a collection of key-value pairs.

student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science"
}

print(student)

# Access values
print(student["name"])  
print(student["age"])   

# Add new key-value pair
student["level"] = "200"
print(student)

# Remove a key-value pair
del student["course"]
print(student)

# Loop through keys and values
for key, value in student.items():
    print(key, ":", value)



#LECTURE 3
#1. Exceptions
"""Exceptions are things that go wrong within our coding.
Exceptions are problems that arise while your program is running.
Syntax errors generally mean you should double-check that you typed your code correctly."""

#2. Runtime Errors
#Runtime errors refer to those created by unexpected behavior within your code. For example, perhaps you intended for a user to input a number, but they input a character instead. Your program may throw an error because of this unexpected input from the user.

#3. try
#In Python try and except are ways of testing out user input before something goes wrong. 
#For example, consider the following code:
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
#In this code, we attempt to convert user input into an integer. If the user inputs something that cannot be converted into an integer, a ValueError is raised, and the code within the except block is executed.


#3. else
#It turns out that there is another way to implement try that could catch errors of this nature.
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
#In this code, if the user inputs something that cannot be converted into an integer, a ValueError is raised, and the code within the except block is executed. However, if no error is raised, the code within the else block is executed.


#Consider how we can use a loop to prompt the user for x and if they don’t prompt again!
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
#In this code, we use a while True loop to continually prompt the user for input until they provide a valid integer. If a ValueError is raised, we inform the user and prompt again. If no error is raised, we break out of the loop and print the value of x.


#We can make it such that our code does not warn our user, but simply re-asks them our prompting question using 'pass'.
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass


main()
