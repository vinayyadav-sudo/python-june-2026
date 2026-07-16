"""
Object Oriented Programming (OOP)
It is a way of programming that is oriented towards creating entities (objects) using a template (class)

This template is called class
The entities are the objects

Class: is a template/blueprint/mould/design to create objects
A class contains:
    1. Specifications/ properties / attributes
    2. Functionality/ methods

Object: Entity/Instance created using the class

"""


# Creating a class
class MyClass:
    pass

# MyClass is a class in Python

a = 1000
print(type(a))

l1 = [10, 20, 9, 0]
print(type(l1))

# Datatypes in Python are defined as classes
# a is an object of class int
# l1 is an object of class list

# help(list)

## Creating a class for students

class Student:
    pass

# Creating an object
# object_name = ClassName()

s1 = Student()
s2 = Student()

# s1 and s2 are objects of class Student
print(type(s1))
print(type(s2))

# Creating an integer object
b = int(2000)
print(b, type(b))

"""
Method: It is function that is defined inside the class
"""

#help(list)

l1 = [1,2,3]
print(l1)
l1.append(10)
print(l1)

print(f"s1: {s1}") # prints s1: <__main__.Student object at 0x000002606F14CC20>
print(f"s2: {s2}")

# docstring of a class - used to provide information about the class

class Student:
    """
    This class is for students.
    It is used to maintain/manage the information about the students of a college
    """
    pass

# help(Student)

"""
Methods are classified into 3 types:
1. Instance method
2. Class method
3. Static method

Instance method:
Method defined inside a class which is bound to the instance/object
We call instance methods using the object of that class
"""

class Student:
    """
    This class is for students.
    It is used to maintain/manage the information about the students of a college
    """
    
    def studying():
        print("The student studies for 2 hours a day.")

# studying() is an instance method created inside the class Student

s1 = Student()

# Calling studying() => object_name.method_name()
s1.studying()