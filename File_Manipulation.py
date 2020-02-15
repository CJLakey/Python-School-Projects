# This script opens the file example.txt

# and then shows some information using the methods

# associated with the object file.


# In the next instruction we create a pointer to the file (or file object)

# named fileEx. This object will be used in the program to

# manipulate the file example.txt.

# The file is opened for reading only operations.


fileEx = open(r"C:\Users\lakey\PycharmProjects\untitled\PythonTest.txt", "r+")

print("Name of the file: ", fileEx.name)

print("Is this file closed? : ", fileEx.closed)

print("What can I do with this file? : ", fileEx.mode)

fileEx.write("Writing line number 1 to the file")

fileEx.write("Writing line number 2 to the file")

fileEx.close()

fileEx = open(r"C:\Users\lakey\PycharmProjects\untitled\PythonTest.txt", "r")

print ("Is this file closed?: ", fileEx.closed)

fileEx.close()

print("Is this file closed?: ", fileEx.closed)

fileEx = open(r"C:\Users\lakey\PycharmProjects\untitled\PythonTest.txt", "r+")

## fileEx.write("This is a test file used with Python")

position = fileEx.tell()

print("Initial position after file is open : ", position)


text = fileEx.read(10)

print("Read information is : ", text)


position = fileEx.tell()

print("Current position after 10 character were read: ", position)


# Moving the position at the beginning of the file


position = fileEx.tell()

print("Position after seek method is executed : ", position)


fileEx.close()
