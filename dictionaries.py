"""
A dictionary is comma separated key-value pairs enclosed within {}
Each key-value pair is separated by colon(:)
{key1:value1, key2:value2, key3:value3..........}
There is no indexing in dictionaries. To fetch the values from a dictionary, we use keys
keys of a dictionary cannot be a duplicate.values can be anything/duplicate
Dictionaries are mutable
"""
student1 = {'roll' : 101, 'name': 'john', 'percent': 87.5}
print(student1)
print(type(student1))

#Accessing a value from a dictionary
#print(studnet1[0])# keyError: 0
print(student1['name'])

#print(student1[city])# keyError: 'city' => key does not exist

#changing a value of the key
print(student1['percent'])

student1['percent'] = 88.5
print(student1)

#keys of the dictionary should be unique
student2 = {'roll': 102, 'name': 'jill', 'percent': 91.0, 'name': 'carol'}
print(student2)

#Values can be duplicate
marks = {'sub1': 80.0, 'sub2': 87.5, 'sub3': 87.5}
print(marks)

#we cannot change key, but we can delete key

"""
key of a dictionary cannot be mutable datatypes. keys should only be Immutable
values can be of any datatype

"""
d1 ={1: True, 2: False, 5.5: 5}
print(d1)

d2 = {True: 1, False: 0, None: 0}
print(d2)

#d3 = {[1, 2, 3]: 6, [10, 55]: 65} #Do not allow list as key
#d3 = {{1, 2, 3}: 6, {10, 55}: 65} #Do not allow set as key
#d3 = {{'a': 1, 'b': 2}: 100} #Do not allow dict as key

student4 = {'roll': 103, 'name': 'Alice', 'marks': {'engish': 76.5, 'maths': 81.0, 'python': 91.5}}
print(student1)

print(student1['marks']) 
print(student1['marks'][2])

#from student4, fetch the marks of maths
print(student4['marks'])
print(student4['marks']['python'])

#Length of a dictionary
print(len(student1))
print(len(student2))
print(len(student1))
print(len(student4))

#membership operator
print(student1)

print(101 in student1)

#the membership operator in dictionary checks if the KEY is present or not (NOT THE VALUE)
print('percent' in student1)

