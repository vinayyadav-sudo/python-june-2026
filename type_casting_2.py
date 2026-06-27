print(bool(100))
print(bool(-34.8))

print(bool("Hi"))
print(bool('python'))

# Which value in string will give us False when we typecast it to Boolean?

# Empty string => It is represented as ''
print(bool(''))

print(bool(' '))


# Any valid character including special characters (space, ...) will get converted into True
# Empty string gets converted into False

print(bool(None))

# Converting to string
print(str(100))
print(str(10.5))
print(str(True))
print(str(None))