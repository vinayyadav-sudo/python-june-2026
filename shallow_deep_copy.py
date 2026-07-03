l1 = [3, 4, 1, 6, 8]
print(l1, id(l1))

# help(list)
l2 = l1.copy()
print(l2, id(l2))

l1[0] = 10
print(l1, id(l1))
print(l2, id(l2))

##################

l3 = [1, 2, 3, [10, 20]]
print("l3 =>", l3, id(l3))

l4 = l3.copy() # shallow copy of l3
print("l4 =>", l4, id(l4))

l3[-1][-1] = 0

print("After changing l3 ===>")

print("l3 =>", l3)
print("l4 =>", l4)

"""
When we create a copy of a list and the inner list has the same memory address.
Due to this, the inner list element of the copied list gets changed when we change the original list
This is called Shallow copy.

To avoid this, we do Deep copy.

How to do deep copy?
Using a function called deepcopy. deepcopy is a part of 'copy' module
"""

import copy

l5 = copy.deepcopy(l3) # creates a deepcopy of l3
print(l5)

# change l3 again
l3[-1][0] = 100

print("After changing l3 again ===>")
print("l3 =>", l3)
print("l4 =>", l4)
print("l5 =>", l5)