"""
Conditional statements: statements that contain certain condition(s), that controls the flow of the program.

if statement: It has a condition. and when the condition is True, it executes a block of code.
When the condition is False, it block of code is NOT executed.

if condition:
    statement1
    statement2
    ....
    statementN

"""

"""
Block: It is a group of statements ( a line of program )
Indentation: To create a block in Python, we use whitespaces (spaces) which is called Indentation.
We can use any number of whitespaces for indentation.
But, it is a standard/ convention to use 4 spaces/ a tab for giving indentation.
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
    print("You are eligible to vote and drive")