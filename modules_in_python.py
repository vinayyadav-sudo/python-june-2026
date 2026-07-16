"""
What is a module in Python?
Any Python file with an extension of .py is a module in Python

File => code.py . Module => code

Modules in Python can be:
1. Built-in modules: provided by Python
    a. Needs to be imported. eg: copy, math
    b. No need to import (pre-imported). eg: builtins, io
2. User-defined modules: the modules (python files) that we create
"""

help(print)

# How to import modules? => Using the 'import' keyword
# Syntax: import module_name

import random

# how to use/call a function of an imported module?
# module_name.function_name(arg1, arg2, ...)

# we can use the help() with modules as well


#help(random)

l1 = [4, 3, 7, 5, 0, 1, 8]
random_number = random.choice(l1)
print(random_number)

dice = [1, 2, 3, 4, 5, 6]
my_num = random.choice(dice)
print(f"My number is {my_num}")

coin = ['heads', 'tails']
print("Toss the coin....")
your_choice = random.choice(coin)
print(f"Your choice: {your_choice}")

# randint
print("Random integer between 2 values:")
random_num = random.randint(100, 200)
print(random_num)


# User-defined modules

import my_module

res1 = my_module.is_even(11)
print(res1)

res2 = my_module.add(10, 2)
print(res2)

# my_module.subtract(10, 4) # AttributeError: module 'my_module' has no attribute 'subtract'