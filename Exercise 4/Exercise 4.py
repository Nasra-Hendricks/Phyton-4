# Question 1: Using a for loop with a list
from importlib import import_module

# TODO: Create a list of fruits
fruits= ("banana" , "pineapple" ,"watermelon")

# TODO: Use a for loop to print each fruit in the list
for x in fruits:
    print(x)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
x=1
while x <5:
    print(x)
    x +=1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for square in range(1,11):
    print(square**2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random

# TODO: Create a list of colors
color= ("red" , "black" , "yellow" , "blue" , "white")

# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    print(random.choice(color))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations as math

print(math.add(5, 2))
print(math.subtract(10, 5))
print(math.multiply(4, 4))
print(math.divide(10, 2))

# TODO: Use a while loop to create a simple calculator
def calculator():
    while True:
        print("Enter '+' to add numbers")
        print("Enter '-' to subtract numbers")
        print("Enter '*' to multiply numbers")
        print("Enter '/' to divide numbers")

operation= input ("Enter a function here:")
number1= int(input("Enter a number here:"))
number2= int(input("Enter a number here:"))

if operation== "+":
    print(number1 + number2)
elif operation== "-":
    print(number1 - number2 )
elif operation== "*":
    print(number1 * number2)
else:
    print(number1 / number2)s
















