"""
A function is a block of code that does a specific task when it is called.

Why do we create functions?
For reusability and readability

Built-in functions => Functions that are pre-built. eg: print(), len(), id(), ...
User-defined functions => defined/created by the user  (programmer)
"""

# WAP to check if a number is even or odd
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# perform some other task
print("Hello everyone, we are learning Python!")

# again, we need to check if a number is even or odd

num = 8
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

"""
To check multiple numbers whether they are Even or Odd, we need to write the same logic
again and again.
To reuse the same Even/Odd code/logic at difference places in the program,
we can create a function, give a name to it and use the name of the function to call the logic
written inside the function (again and again)

So, we write this code of block as a function and call this function whenever we want to reuse the logic
"""

# Creating a function

"""
Syntax:

def function_name(arg1, arg2, arg3, ...., argN):
    statement1
    statement2
    ...
    statementN
"""

def greet():
    print("Hello, good evening!")
    print("Have a nice day...")

# The above example is a user-defined function with 'greet' as function name and NO arguments

# Calling a function

l1 = [1,2,3,4]
print(len(l1))

greet()

# help(len)

def greet_person(name):
    print(f"Hello {name}, good evening...")

greet_person("John")

# The above function name => greet_person. Number of arguments -> 1

greet_person("Jill")
greet_person("Mark")

"""
greet_person() # TypeError: greet_person() missing 1 required positional argument: 'name'

The value for the 'name' argument needs to be passed while calling the function,
else we get an Error!!
"""

def add(num1, num2):
    result = num1 + num2
    print(result)

add(10, 6)

# add(10) # TypeError: add() missing 1 required positional argument: 'num2'
# add() # TypeError: add() missing 2 required positional arguments: 'num1' and 'num2'
# add(6, 7, 1) # TypeError: add() takes 2 positional arguments but 3 were given

"""
Documentation of a function -> docstring

The docstring is a helper message that is written inside the function for others to know what the function does
How to write doctring?
docstring is written using triple quotes at the top of the function defination
We cannot write anything above it
"""
help(len)

help(add)

def add(num1, num2):
    '''
    Adds 2 numbers and prints the result
    '''
    result = num1 + num2
    print(result)


help(add)

"""
Question: Create a function in Python to check if an integer is Even or Odd
Write docstring in the function
"""

def even_odd(number):
    """
    This function takes an integer and prints whether that integer is Even or Odd
    """
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

help(even_odd)


"""
return: keyword used to return any value from a function, outside the function
"""
even_odd(10)

add(10, 3)


# print(result) # NameError: name 'result' is not defined

"""
Since the 'result' variable is defined inside the function 'add', we cannot use it outside the function
If we want to use the value of 'result' variable, we need to return that value from that function
"""

output = add(16, 7)
print(output)

"""
When a function does not return any value, we get None
"""

# returning value from function
def add(num1, num2):
    '''
    Returns the addition of 2 numbers
    '''
    result = num1 + num2
    return result

print("Adding 5 and 3")
res = add(5, 3)
print(res)