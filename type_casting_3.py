l1 = [3, 8, 9, 2, 0, 7]
print(l1)
print(type(l1))

print(tuple(l1))
print(l1)

l1 =tuple(l1)
print(l1)
print(type(l1))

fruits = ('mango', 'apple', 'banana', 'grapes')
print(fruits,type(fruits))

fruits = list(fruits)
print(fruits, type(fruits))

fruits =set(fruits)
print(fruits, type(fruits))

nums = [6, 3, 0, 5, 6, 8, 6, 7, 7, 6]
print(nums, type(nums))

nums1 =set(nums)
print(nums1) #only unique elements are there.

print(nums)

print(list(set(nums)))


