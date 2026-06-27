"""
List is a collection/sequence of comma separated items/elements enclosed within []
The elements can be of any datatype (heterogenous)
Duplicate elements are allowed in a list
Lists are ordered: the elements of the list remain in the same order in which we create it (unless we change it)
"""

groceries = ["Rice", "Pulses", "Salt", "Spices"]
print(groceries)
print(type(groceries))

marks = [78.5, 81.0, 82.5]
print(marks)
print(type(marks))

student1 = [101, "John", 84.5]
print(student1)
print(type(student1))

list_1 = [100, 8.5, 'Python', None, False, True, 100, 'Hello']
print(list_1)

"""
len() function
It is used fetch the total number of items/elements in a list/collection
"""

print(len(list_1))
print("Number of grocery items are", len(groceries))

"""
Indexing of lists: Positioning of lists
Accessing the elements of the list using index (its position)
Every element in a list has a index
Index starts from 0 and ends at length-1
How to access any element using using indexing? => list[index]
"""
student1 = [101, "John", 84.5]
print("Roll number is", student1[0])
print("Name of the student is", student1[1])
print("Marks of the student is", student1[2])
# print(student1[3]) # IndexError: list index out of range

"""
Positive index: 0 to length-1 (Left to Right)
Negative index: -1 to -length (RIght to Left)
"""

list_1 = [100, 8.5, 'Python', None, False, True, 100, 'Hello']
print("Last element:", list_1[-1])
print("Second last element:", list_1[-2])

"""
Concatenation of lists => Joining lists together
"""

batch1 = ["Alice", "John", "Mark", "Dan"]
batch2 = ["Jill", "Bob", "Carol"]
combined_batch = batch1 + batch2
print("Merging/Joining the batches (Conatenation): ", combined_batch)

# The sequence of the lists will be maintained

"""
Repetition of lists
"""
print(batch2 * 2)

"""
Mutability: The ability of a datatype to change itself.
Lists are MUTABLE => We can change them after we have created them.
- We can change/modify a specific element of a list
- Add new element(s)
- Delete an existing element from the list
"""

print(marks)
print("Memory address before change", id(marks))
print("Value before change:", marks[0])

marks[0] = 79.5
print("Value after change:", marks[0])
print(marks)
print("Memory address after change", id(marks))

# Memory address after the change will remain same

"""
marks[0] = 79.5 => Mutability
marks = [79.5, 81.0, 82.5] => Re-assignment
"""

"""
Membership operator on lists: in, not in
In lists, it checks if the element is present or not
"""

print(combined_batch)

# Check if "Jack" is a student?
print("Jack" in combined_batch)
print("Jill" in combined_batch)

list_2 = [10, 20, 30, 10, '10', 100, '50']
print(10 in list_2)
print('10' in list_2)
print(500 in list_2)
print(50 in list_2)
print('50' in list_2)