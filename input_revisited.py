marks = 78
print("The student obtained:", marks)
marks = marks + 5
print("New marks is", marks)

age = input("Enter your age: ")
print("Your age is", age)

# Increase the age by 1 and store it back to the same variable - age
# age = age + 1 # input() function always accepts the value as a string!!!!

print("Datatype of age:", type(age))

# So, how do we add 1 to age? => We first convert age to int and then add 1 to it..
age = int(age) + 1
print("Next year, your age will be", age)

print("new datatype of age:", type(age))