"""
while loop is a conditional based loop.
While loop is created using a condition and it executes a block of code repeatedly until the 
given condition is True
Once the condition becomes False, the loop stops/exits/terminates

Syntax:

while condition:
    statement1
    statement2
    ...
    statementN
"""

# WAP to print numbers from 0 to 9
for i in range(10):
    print(i)

# we can get the same output using while

print("using while loop")
num = 0
while num < 10:
    print(num)
    num += 1 # num = num + 1


# Infinie loop => when the loop keeps on executing infinitely
# When the condition in while loop never becomes False, it leads to an iinfinite loop

num = 0
while num < 10:
    print(num)
    num += 2

# for i in range(0, 10, 2):
#     print(i)

# WAP to print 10 to 1 using while loop
print("Printing 10 to 1 using while loop:")

num = 10

while num > 0:
    print(num)
    num -= 1
print("Happy New Year!!")

# while loop controlled by user input

choice = input("Do you want to calculate length of a string? (y/n): ")
while choice == 'y':
    s1 = input("Enter a string: ")
    print(f"Number of characters in the string are: {len(s1)}")
    choice = input("Do you want to continue? (y/n): ")