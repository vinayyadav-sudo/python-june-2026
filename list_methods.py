"""
Adding new elements to a list
"""

student1 = [101, "John", 78.5]
print(student1)

# append() method => adds an element to the end of the list
student1.append("Delhi")
print(student1)

# student1.append(100, 200) # TypeError: list.append() takes exactly one argument (2 given)
student1.append(1234567890)
print(student1)

# List itself can be an element of another list
student2 = [102, "Jill", 81.0, ["Eng", "Maths", "Python"]]
print(student2[2])
print(student2[-1][1])

student1.append(["Eng", "Maths", "Python"])
print(student1)

# extend() method => it takes only a collection as an argument and adds each element of that collection at the end of list one by one
student1.extend(["Dance", "Chess"])
print(student1)

# student1.extend(170) # TypeError: 'int' object is not iterable
student1.extend("Cricket") # Each character of the string gets added one by one at the end of the list!!!!
print(student1)

student1.append("Cricket")
print(student1)

# insert(index, value) method => adds a single element before the given index
student1.insert(3, "Mumbai")
print(student1)

"""
Deleting elements from a list
"""

# remove() -> removes/deletes the first occurance of the given element from the list
list_1 = [5, 3, 6, 10, 9, 1, 0, 10, 10, 10]
print("Original list_1", list_1)

list_1.remove(6)
print("Deleted 6", list_1)

list_1.remove(10)
print("Deleted 10", list_1)

student1.remove("Delhi")
print(student1)

# student1.remove(3, 1) # TypeError: list.remove() takes exactly one argument (2 given)
# We cannot delete more than 1 value at once.

# pop() method => deletes the element on the given index
print(list_1)

list_1.pop(2) # value at index 2 gets deleted
print(list_1)

# list_1.pop(0, 1) # TypeError: pop expected at most 1 argument, got 2
# We cannot delete more than 1 element using pop() as well

# student1.remove() # TypeError: list.remove() takes exactly one argument (0 given)
# remove() requires the value that needs to be deleted

list_1.pop() # it deletes the value at index -1 (last index value)
print(list_1)

# if we do not give any index to pop(), it deletes the value at last index

"""
To view all the functions/methods of a datatype
"""

# help(list)

# count() method => counts the occurances of an element in a list
list_2 = [5, 'hi', 8.5, 5, 5, 'hi', 'python', False, 5]

print(len(list_2))

print("Occurances of 5 in list_2:", list_2.count(5))
print("Occurances of 'hi' in list_2:", list_2.count('hi'))
print("Occurances of 100 in list_2:", list_2.count(100))

# index() method => returns the index of a value (first occurance only)
print(list_2)
print("Index of 8.5 is:",list_2.index(8.5))
print("Index of 5 is:", list_2.index(5))

# sort() method
list_3 = [6, 8, 0, -4, 9, 4, 3]
print("list_3: ", list_3)
list_3.sort() # sort the list in ascending order
print("After sorting in ascending order:", list_3)

# what about sorting the list in descending order?
list_3.sort(reverse=True)
print("After sorting in descending order:", list_3)

"""
clear()
copy()
reverse()
"""