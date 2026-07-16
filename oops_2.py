class Student:
    """
    This class is for students.
    It is used to maintain/manage the information about the students of a college
    """
    
    def studying(arg1): # we need an argument to accept the object being passed
        print("The student studies for 2 hours a day.")

# studying() is an instance method created inside the class Student

s1 = Student()

# Calling studying() => object_name.method_name()
s1.studying()

"""Whenever we call an instance method using the object, Python passes the object itself as 
the first argument of tha method. This is why instance method are called to be bound to the
instance/object

And this argument has a convention/standard name => self

Hence, every instance method will have the first argument as 'self'
"""

# help(list)

class Student:
    """
    This class is for students.
    It is used to maintain/manage the information about the students of a college
    """
    
    def studying(self): # self is the convention for accepting the object
        print("The student studies for 2 hours a day.")
        print(f"self => {self}")


st1 = Student()
st1.studying()

print(f"st1 => {st1}")

# self represents the object inside the instance method

print("Adding arguments to the instance method")

class Student:
    """
    This class is for students.
    It is used to maintain/manage the information about the students of a college
    """
    
    def studying(self, hours): # self is the convention for accepting the object
        print(f"The student studies for {hours} hours a day.")
        print(f"self => {self}")


st1 = Student()
# st1.studying() # TypeError: Student.studying() missing 1 required positional argument: 'hours'
st1.studying(3)

st2 = Student()
st2.studying(2)

####

"""
Initializer or the __init__() method

It is a special type of instance method.
It is used to create and initialize the attributes/properties/variables of the objects
It helps to create instance variables while creating the object
"""

print("\n==================================\n")

class Student:
    """
    This class is for students.
    It is used to maintain/manage the information about the students of a college
    """

    def __init__(self):
        print("Calling the initializer!!")
    
    def studying(self, hours): # self is the convention for accepting the object
        print(f"The student studies for {hours} hours a day.")

        


s1 = Student()

# When we create an object of a class, __init__() method gets automatically called by Python (if it exists)

# Creating instance variables/properties/attributes

class Student:
    """
    This class is for students.
    It is used to maintain/manage the information about the students of a college
    """

    def __init__(self, roll_num, name, sub):
        print(f"Calling the initializer!! => {self}")
        # self.variable = value
        self.roll = roll_num
        self.name = name
        self.subject = sub

    
    def studying(self, hours): # self is the convention for accepting the object
        print(f"The student studies for {hours} hours a day.")

s1 = Student(101, "John", "Maths")
s2 = Student(102, "Jill", "English")
s3 = Student(103, "Mark", "Python")

# roll, name and subject => instance variables/properties/attributes