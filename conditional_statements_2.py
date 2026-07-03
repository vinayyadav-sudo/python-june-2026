"""
What if we want to do something else when the condition is False?
Then, we use 'else'
"""

# age = int(input("Enter your age: "))
age = 19

if age >= 18:
    print("You are an adult")
    print("You are eligible to vote and drive")
else:
    print("Not eligible!!")

"""
What if, we want to check multiple conditions in the same scenario? => We use 'elif'
For example, we want to print the grade of a student depending on the marks secured
If the marks is 90 or more -> Grade -> A
If marks is between 80 and 89 (both included) -> Grade -> B
If marks is between 70 and 79 (both included) -> Grade -> C
If marks is between 60 and 69 (both included) -> Grade -> D
If marks is below 60 -> Graded -> F
"""

marks = 91

if marks >= 90:
    print('A')
elif marks >= 80 and marks < 90:
    print('B')
elif marks >= 70 and marks < 80:
    print('C')
elif marks >= 60 and marks < 70:
    print('D')
else:
    print('F')

# Indentation Error - we get this when there is some issue with Indentation

"""
Nested if-elif-else
if-elif-else block inside another if-elif-else block

For example, we need to find the grade only when the marks obtained is less than or equal to 100
"""

marks = 104
if marks <= 100:
    if marks >= 90:
        print('A')
    elif marks >= 80 and marks < 90:
        print('B')
    elif marks >= 70 and marks < 80:
        print('C')
    elif marks >= 60 and marks < 70:
        print('D')
    else:
        print('F')
else:
    print("Invalid marks!! Marks should be between 0-100")


#######

is_organizer = input("Are you in the organizing committee? (y/n): ")
has_ticket = input("Do you have a valid ticket? (y/n): ")

if is_organizer == 'y' or has_ticket == 'y':
    print("You can enter the event")
else:
    print("Not allowed to enter!!")

"""
Write a program (WAP) to check if an integer is positive or negative
"""

num = 4

if num < 0:
    print("Negative")
else:
    print("Positive")

"""
WAP to check if an integer is even or odd
Even - integer divisible by 2
Odd - integer NOT divisible by 2
"""

num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    print("Even number")
else:
    print("Odd number")

"""
Syntax of if-else:
if condition:
    if_block
else:
    else_block
"""


"""
Ternary operator in Python -> Single line if-else
Syntax:
if_block if condition else else_block
"""

num2 = 21
print("Even number") if num2 % 2 == 0 else print("Odd number")