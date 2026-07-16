"""
Python classifies files into 2 types:
1. Text files => files that contain plain text/ characters. eg: text file, log file
2. Binary files => contents of the file are in bytes (1 byte = 8 bits). eg: video, audio, image
"""

# Opening a file => open()

# help(open)

"""
Modes for opening a file:
r -> read mode
w -> write/overwrite mode
x -> create mode
a -> append mode

t -> text mode
b -> binary mode
"""

file_handler = open("loops.py", "rt") # 'tr'

# 'rt' means opening a text file in read mode ( for reading )

# If the file does not exist, we get FileNotFoundError

print(file_handler)

# Closing a file => close()
file_handler.close()

# Reading a file => read()

file_handler = open("loops.py", "rt") # opens the file in read mode
data = file_handler.read() # reads the entire contents of the file as a string
file_handler.close() # closes the file

print(data)
print(type(data))

# Creating file -> to create a file, we need to open the file with 'x' mode
# fh = open("file1.txt", "xt") # creates and opens the file => file1.txt

"""
If we try to create a file which already exists, we get an error =>
FileExistsError: [Errno 17] File exists: 'file1.txt'
"""

"""
fh = open("file3.txt", "xt")
# Writing into files => write()
fh.write("Hello everyone, good evening!\nWe are learning file handling with Python.\nGood bye...")
fh.close()
"""

# 'w' mode => overwrite a file (deletes the existing contents & write new contents)

fh = open("file2.txt", "wt")
fh.write("This is a new content.\nWe have used 'w' mode.")
fh.close()

# 'a' mode => append mode => adds new content at the end of the file

fh = open("file2.txt", "at")
fh.write("\nAdding new content using 'a' mode.")
fh.close()


"""
Common errors with file handling

1. If we open the file with 'r' mode, we cannot use write() function
fh = open("file2.txt", "rt")
fh.write("Hello") # io.UnsupportedOperation: not writable
fh.close()

2. If we open the file with 'w'/'x'/'a' mode, we cannot use read() function
fh = open("file2.txt", "at")
x = fh.read() # io.UnsupportedOperation: not readable
fh.close()

3. Opening a file in 'x' mode if the file already exists

4. Opening a file in 'r' mode if the file does not exist
"""

# readlines()

fh = open("file3.txt", "rt")
contents = fh.readlines()
fh.close()

print("readlines() output =>")
print(contents)
print(type(contents), len(contents))


# WAP to count the occurance of 'e' in the file file3.txt
fh = open("file3.txt", "rt")
contents = fh.read()
fh.close()
e1 = contents.count('e')
print(f"Occurance of 'e' in file3.txt: {e1}")

# WAP to count the occurance of 'e' in each line of file file3.txt
fh = open("file3.txt", "rt")
contents = fh.readlines()
fh.close()

print("Occurance of 'e' in each line of file3.txt =>")
for line in contents:
    print(line.count('e'))

# with statement

with open("file3.txt", "xt") as fh:
    content = fh.read()

# Python closes the file automatically when we use 'with' statement
print(content)