"""
Fundamental datatypes are:
1. Integers => int => whole numbers (postive numbers/negative numbers/0). Examples: 0, 100, 45, -64
2. Floats => float => Fractional numbers => 55.3, 89.34123, -3.7, 5.0
3. Strings => str => a group/sequence of characters enclosed with quaotations. 
    Examples: 'Hello everyone', "Python", '''Python is fun'''
4. Boolean => bool => True/False
5. Special type => NoneType => None

type() function => it returns/tells the datatype of a value/variable
"""

# Integers
age = 20
print(age)
print(2000)

print(type(age))
print(type(2000))

# Floats
marks = 85.5
print(marks)
print(type(marks))

# Strings
name = "John Cena"
print(name)
print(type(name))

address = 'house number 7, ABC street, Delhi'
print(address)
print(type(address))

language = '''Python 3.14'''
print(language)
print(type(language))

# message = 'This is Python's class'
message = "This is Python's class"
print(message)

full_address = """House number 7,
ABC street,
Bangalore - 01,
Karnataka"""

print(full_address)
print(type(full_address))

number = "10" # this is a string because it is enclosed within quotes!!!
print(type(number))

percent = '74.5'
print(type(percent))

# print(We are learning Python) => ERROR!!! Do not forget quotes

# Boolean - True, False

is_active = True
print(is_active)
print(type(is_active))

value = "True"
print(type(value))

eligible_to_vote = False
print(eligible_to_vote)
print(type(eligible_to_vote))

# var = true => ERROR

# Special datatype
val = None
print(val)
print(type(val))