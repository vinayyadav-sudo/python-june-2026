"""
Membership operator - continued..
not in: returns True if the item is ABSENT/ NOT PRESENT in the collection
"""

s1 = "We are learning Python"
print("Python" not in s1)
print("z" not in s1)

print(10 * 2 + 5)
print(10 * 2 ** 3)
print(10 + True and False)
print(True or False and False)

"""
Precedence: If there are 2 or more expressions in the same operation,
precedence decides the priority of which operation will happen first.
- Precedence tells which operator has high or low priority.

There is a Precedence Table using which Python decides the priority:
()
**
/, //, %, *
-, +
Membership operators, Comparison operators
not
and
or
"""

print((True or False) and False)

######

print(2 ** 1 ** 3)

"""
Associativity: When the precedence of 2 operators are same, then
associativity decides whether do perform the operation Left to Right OR Right to Left

For most of the operators, associativity is Left to Right
For ** operator, associativity is Right to Left
"""

print(10 / 2 % 2)