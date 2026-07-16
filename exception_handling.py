# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# result = num1 / num2
# print(result)

# Error/Exception handling in Python is done using try-except blocks

"""
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    result = num1 / num2 # ZeroDivisionError
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be 0")
except ValueError:
    print("Invalid input, only integers are allowed.")
"""

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    result = num1 / num2 # ZeroDivisionError
    print(result)
except Exception:
    print("Some error occured")
except ZeroDivisionError:
    print("Denominator cannot be 0")
except ValueError:
    print("Invalid input, only integers are allowed.")

    
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    result = num1 / num2 # ZeroDivisionError
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be 0")
except ValueError:
    print("Invalid input, only integers are allowed.")
except Exception:
    print("Some error occured")

# else and finally blocks
"""
else block gets executed when there is no error / exception in the code
finally block gets executed always
"""

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    result = num1 / num2 # ZeroDivisionError
except ZeroDivisionError:
    print("Denominator cannot be 0")
except ValueError:
    print("Invalid input, only integers are allowed.")
except Exception:
    print("Some error occured")
else:
    print("No error occured")
    print(result)
finally:
    print("Runs always")