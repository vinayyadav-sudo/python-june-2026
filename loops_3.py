"""
break: it is used to terminate/stop/exit the loop
"""

num = 0
while num < 10:
    print(num)
    num += 1
    if num == 5:
        break


fruits = ["mango", "chiku", "guava", "banana", "apple", "grapes"]
for f in fruits:
    if f.startswith("g"):
        break
    print(f)


"""
continue: it is used to skip an iteration in a loop and continue with the next iteration
"""
print("continue =>")
for f in fruits:
    if f.startswith("g"):
        continue
    print(f)


"""
Problems using loops
"""

nums = [8, 3, 2, 1, 5]

# Which is lowest/minimum/smallest value in the list nums?
# WAP to find the minimum value in a list

minimum = nums[0]

for i in nums:
    if i < minimum:
        minimum = i

print(f"Minimum value in the list: {minimum}")

nums = [8, 3, 2, 11, 1, 5]
# WAP to find the maximum value in the given list

maximum = nums[0]
for i in nums:
    if i > maximum:
        maximum = i
print(f"Maximum value in the list: {maximum}")


"""
WAP to count the number of each character in a string and store the it in a dictionary
Example:
s1 = "www.google.com"
Output: {'w':3, '.': 2, 'g':2, 'o':3, 'l':1, 'e':1, 'c':1, 'm':1}
"""
s1 = "www.google.com"
out = {}
for char in s1:
    if char in out:
        out[char] = out[char] + 1
    else:
        out[char] = 1

print(out)

#######

nums = [4, 1, 3, 6]
# output = [16, 1, 9, 36]
squares = []

for i in nums:
    x = i ** 2
    squares.append(x)

print(squares)