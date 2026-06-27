"""
Tuples are comma separated elements enclosed within ()
The elements of a tuple can be of any datatype (heterogenous)
Duplicate elements are allowed in a tuple
Tuples are ordered: the elements of the tuple remain in the same order in which we create it
Tuples are IMMUTABLE (cannot be modified)
"""

t1 = (10, 7.5, "hello", True, 10, None, "python", 10)
print(t1)
print(type(t1))

# Indexing
print(t1[0])
print(t1[-1])

# length?
print(len(t1))

# Tuples are immutable, we cannot change them
# t1[0] = 11 # TypeError: 'tuple' object does not support item assignment

weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
weekends = ("Sat", "Sun")

print(weekdays, type(weekdays))
print(weekends, type(weekends))

# Concatenation of tuples => joins tuples together and return a new tuple
days = weekdays + weekends
print(days)

# Repetition
print(weekends * 3)

# Membership operator
print("Mon" in weekdays)
print("Sun" in weekends)
print("Sat" in weekdays)
print("Thu" not in weekdays)

# Methods of Tuple

# help(tuple)

"""
count() method => counts the number of occurances of a given element
"""

t2 = (1, 2, 3, 4, 5, 1, 5, 6, 7, 3, 1, 1, 2)
print(t2.count(1)) # counts how many times 1 occurs in the tuple t2
print(t2.count("hello"))

"""
index() method => gives the index of the given value
"""

print(days)
print(days.index('Fri'))

print(t2)
print(t2.index(5))
