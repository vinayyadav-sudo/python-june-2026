"""
Type casting: converting a datatype to another datatype
"""

age = 25
print(type(age))

# What will be the float equivalent of 25? => 25.0
print(float(age))

print(age, type(age))

age = float(age)
print(age, type(age))


percent = 78.57
print(percent, type(percent))

# Can we convert percent to int?
print(int(percent)) # removes the fractional part of the float value


# round() => to round off a float
rounded_percent = round(percent)
print(rounded_percent)

percent1 = 78.45
rounded_percent1 = round(percent1)
print(rounded_percent1)

marks = "56.43"
print(marks, type(marks))

# Can we convert marks into float? => 56.43
marks = float(marks)
print(marks, type(marks))

marks = "56.43"
# Can we convert marks (str) into int? => 56?
# marks = int(marks) => ValueError: invalid literal for int() with base 10: '56.43'

# To convert a string into an integer, the string SHOULD ONLY contain digits (0-9) in it

roll_number = "12345"
print(roll_number, type(roll_number))

roll_number = int(roll_number) # this will work because the string contains digits ONLY
print(roll_number, type(roll_number))

language = "Python3.14"
print(language, type(language))

# Can we convert language to float?
# print(float(language)) => ValueError: could not convert string to float: 'Python3.14'

# Can we convert "56.43" (string) into 56 (int)?
# Yes, we can. First convert "56.43" (string) to 56.43 (float) and then convert it to 56 (int)

print(int(float("56.43")))

reg_number = 123456
# We we covert reg_number into string?
reg_number = str(reg_number)
print(reg_number, type(reg_number))

sub1_marks = 76
# We we covert sub1_marks into float?
sub1_marks = float(sub1_marks)
print(sub1_marks, type(sub1_marks))

is_active = True
# Can we convert is_active to int?
print(int(is_active))

is_running = False
print(int(is_running))

"""
True => 1, 1.0
False => 0, 0.0
"""
print(float(is_active))
print(float(is_running))

print(str(is_active)) # "True"
print(str(is_running)) # "False"


######

ram = 8
print(bool(ram))

cpu = 5
print(bool(cpu))

max_percent = 100
print(bool(max_percent))

marks_obtained = -10
print(bool(marks_obtained))

"""
All positive and negative integers can be converted into bool and they result in True
Which integer will give us False? => 0
"""

value = 0
print(bool(value))

print(bool(10.5))
print(bool(-10.5))
print(bool(0.0))