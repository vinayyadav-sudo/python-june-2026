"""
Loops: are used to perform a task repeatedly
Loops in Python:
1. for loop
2. while loop

1. for loop - Iterator based loop
It steps through the elements/items of an iterable object (list/str/tuple/set/dict) one by one and
executes a block of code repeatedly for a number of times equal to the length of the iterable object

Syntax:

for var in iterable_object:
    statement1
    statement2
    ....
    statementN

REST OF THE CODE
"""

profits = [11, 8, 7, 10]
# print(profits[0])
# print(profits[1])
# print(profits[2])
# print(profits[3])

for p in profits:
    print(p)
print("Bye")

fruits = ("Mango", "Apple", "Chiku", "Orange", "Banana", "Grapes")

for f in fruits:
    print(f)
