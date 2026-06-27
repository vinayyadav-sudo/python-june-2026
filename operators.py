"""
What is an Operator?
Symbols that perform some operation on value/variable (operands)
Example:
a = 10
b = 5
a * 2 + b => '*' and '+' are operators. a, 2, b are operands
"""


# Types of Operators bases on the operation that we are performing

"""
Arithmetic operator: Used for mathematical operations/calculations
"""
x = 10
y = 3
print("x=", x)
print("y=", y)

print("x + y =", x + y) # Addition
print("x - y =", x - y) # Subtraction
print("x * y =", x * y) # Multiplication
print("x / y =", x / y) # Division => Full division (float)
print("x // y =", x // y) # Floor/Integer division => gives quotient
print("x % y =", x % y) # Modulus operator => gives remainder
print("x ** y =", x ** y) # Exponential/power operator => x to the power y

# Can we perform arithmetic operations between int and float? => YES
print(10.5 + 9)

# Can we perform arithmetic operations between int and str? => NO
# print(10 + '5') # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Can we perform arithmetic operations between int and bool? => 
print(10 + True)

"""
Question: Write a Python code to take 2 integers as inputs from the user and then add them
"""
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)

"""
If we apply '+' operator with 2 strings, both the strings get joined together.
This is called Concatenation of strings!!!
"""

num1 = input("Enter a number: ")
num1 = int(num1)
num2 = input("Enter another number: ")
num2 = int(num2)
result = num1 + num2
print(result)

# We can convert the input to int in the same line as input() function
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 + num2
print(result)

"""
Question: Write a Python code to take 2 integers as inputs from the user and then divide first int with second
"""
print("Division =>")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 / num2
print(result)

"""
If we divide any number with 0, we get 'ZeroDivisionError'
Example: 
10 / 0 => ZeroDivisionError: division by zero
"""