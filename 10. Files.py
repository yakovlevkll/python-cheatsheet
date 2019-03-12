import sys
import os

# FILE I/O

# Best practice for handling files
with open("0. Installation.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)

'''
There are several opening modes
r - reading
r+ - reading and writting
'''

# Get the file mode used
print(f.mode)

# Get the files name
print(f.name)

# Write text to a file with a newline
f.write('Some text')

# Close the file
f.close()

# Read text from the file
f.read()


# OS

os.remove("test.txt")  # will remove a file.
os.rmdir()  # will remove an empty directory.
shutil.rmtree()  # will delete a directory and all its contents.
