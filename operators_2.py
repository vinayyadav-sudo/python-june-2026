# Assignment operator => =

var = 500 # the right side value gets assigned to left side variable
print(var)

# Compound assignment operators: +=, -=, /=, //=, %=, **=
var += 100 # value = value + 100 => Adds 100 to var and assigns it back to var
print(var)

var -= 50
print(var)

var *= 2
print(var)

var /= 11
print(var)

var //= 5
print(var)

# If one of the operand is a float, the outpu will be also a float

"""
Comparison operators/ Relational operators
Used to compare 2 operands and the output is a Boolean - True/False
== -> Equality operator - checks if one value is equal to another
< -> Less than operator
> -> Greater than operator
<= -> Less than or equal to operator
>= -> Greater than or equal to operator
!= -> Not equal to
"""

a = 100
b = 99
c = 100

print("Comparison Operators => ")

# == returns True if the left side value is equal to the right side value
print(a == b)
print(a == c)

# != returns True if the left side value is NOT equal to the right side value
print(a != b)
print(a != c)

# >
print(a > b)
print(a > c)
print(b > c)

# <
print(a < b)
print(a < c)
print(b < c)

# >=
print(a >= b)
print(a >= c)
print(b >= c)

# <=
print(a <= b)
print(a <= c)
print(b <= c)

#########################

"""
Logical Operators: and, or, not
They operate on Boolean values
"""
print("Logical Operators => ")

# and
"""
True and True => True
True and False => False
False and True => False
False and False => False
"""

print("and =>")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or
"""
True or True => True
True or False => True
False or True => True
False or False => False
"""

print("or =>")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not => inverts the value
# not True => False
# not False => True

print("not =>")
print(not True)
print(not False)


"""
Membership operator
This checks if an item is present inside a sequence/collection (example: string)
in: returns True if the item is present in the collection, else it returns False
not in:
"""
print("Membership Operators => ")

s1 = "We are learning Python"
print("Python" in s1)
print("P" in s1)
print("p" in s1)
print("Java" in s1)
print("learn" in s1)


# Sub-string => Part of a string

print("ar" in s1)
print("ho" in s1)
print("el" in s1)
print("e l" in s1)