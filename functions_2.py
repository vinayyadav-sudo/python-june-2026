# Returning multiple values from a function

def arithmetic(num1, num2):
    add = num1 + num2
    return add
    sub = num1 - num2
    return sub
    multiply = num1 * num2
    return multiply

result = arithmetic(10, 5)
print(result)

# the above function does not return multiple values. It comes out from the first return itself

def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    return add, sub, multiply

result = arithmetic(10, 5)
print(result)
print(type(result))

"""
We can return multiple values from a function by separating them with comma.
When we do that, the values get stored as a tuple
While creating a tuple, () are optional
"""

print(f"Addition output: {result[0]}")
print(f"Subtraction output: {result[1]}")
print(f"Multiplication output: {result[2]}")

# Types of arguments in a function

# Positional arguments - arguments that take the values by their position

def add(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    return a + b + c

print(add(4, 2, 8))

# print(add(10, 20)) # TypeError: add() missing 1 required positional argument: 'c'
# positonal arguments are mandatory

# Default arguments - arguments that has some default value

def add(a, b, c=1):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    return a + b + c

"""
While creating a function, we can provide a value to one or more arguments
For the arguments for which we provide default value are called default arguments.
Here, in the above function, 'c' is a default argument
"""

print(add(10, 20, 30))
print(add(10, 20))

"""
If we do not provide the value of a default argument while calling the function, we don't get an error
Rather, we the default value gets utilized
Since, 'c' is a default argument, it becomes optional
"""

def add(a, b=0, c=1):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    return a + b + c

print(add(10))

def add(a=0, b=0, c=1):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    return a + b + c

print(add())
print(add(4))
print(add(10, 20))
print(add(1, 3, 5))
# print(add(1, 2, 3, 4))

"""
lambda: keyword to create a single line function
This is also called Anonymous function because when we create it, we do not write a function name

Syntax:
lambda arg1, arg2, ...: expression
"""

def square(num):
    return num ** 2

print(square(5))

sq = lambda num: num ** 2

# No function name
# No return keyword is used to return the value
# The value gets automatically returned

print(sq(4))