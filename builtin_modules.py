import math

# help(math)
res1 = math.sqrt(100)
print(res1)

# print(pi) # NameError: name 'pi' is not defined
print(math.pi)

radius = float(input("Enter the radius of the circle: "))
area = round(math.pi * radius ** 2, 2)
print(f"Area of the circle with radius {radius} is {area}")

# Factorial of a number?
# n! => (n-1) * (n-2) * .... * 1
# 4! => 4 * 3 * 2 * 1 = 24

num = int(input("Enter a number: "))
fact = math.factorial(num)
print(f"Factorial of {num} is {fact}")

"""
datetime module
This modules is used to work with dates, time, date-time combinations
"""

import datetime

# Importing only date class - when we want to work only with dates
# from datetime import date

# Importing only time class - when we want to work only with time
# from datetime import time

today = datetime.date.today()
print(f"Today's date is {today}")

print(today.year)
print(today.month)
print(today.day)

# Current date and time
now = datetime.datetime.now() # current date and time
print(now)

print(now.hour)

# Current time only
time_now = datetime.datetime.now().time()
print(f"Current time is {time_now}")

# Creating a specific date
# Example: Independence day => 15th August 1947
independence_day = datetime.date(1947, 8, 15) # YYYY-MM-DD
print(f"India got independence on {independence_day}")

# Formatting the date => strftime() => converts the datetime object into formatted string

x = independence_day.strftime("%d-%m-%Y") # DD-MM-YYYY
print(x)

print(independence_day.strftime("%d-%B-%Y"))
print(independence_day.strftime("%d-%b-%Y"))
print(independence_day.strftime("%d-%b-%y"))

# Converting a string to datetime format => strptime
date1 = "26-01-1950"
print(date1, type(date1))

date1_obj = datetime.datetime.strptime(date1, "%d-%m-%Y")
print(date1_obj, type(date1_obj))


# WAP to find out the age of someone using their birthday
birthday = input("Enter your birthday in yyyy-mm-dd format (eg: 2000-01-01): ")
birthday_obj = datetime.datetime.strptime(birthday, "%Y-%m-%d")
print(birthday_obj)
today_date = datetime.datetime.today()

# age = (today_date.year - birthday_obj.year)
age = (today_date - birthday_obj)
print(f"Your age is {age} years")