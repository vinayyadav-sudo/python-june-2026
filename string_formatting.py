"""
String formatting using f-string
"""
age = 20
name = "John"

# output => John is 20 years old.
print(name, "is", age, "years old.")
print(f"{name} is {age} years old.")

percent = 81.5

# output => John who is 20 years old secured 81.5% marks.
print(name, 'who is', age, "years old secured", percent, "% marks.")
print(f"{name} who is {age} years old secured {percent}% marks.")