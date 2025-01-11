# 7 basic data types
# Integers are any signed whole number.
myInt = 5
# Floats are any real number which isn't an integer, such as 1.5 or 2.25. Has 64 bit precision.
myFloat = 5.2
# Strings are sequences of characters which are stored as one variable, often used for sentences.
myStr = "This is a string."
# Booleans are true or false. 
myBool = True
# Lists are collections of any other variable in order. Each individual entry has its own index starting at 0. Initiated with square brackets. Mutable. 
myList = [0, 1, "two", 3.2, False, 1, 1]
# Tuples are similar to lists, but are immutable, meaning they cannot be changed when they are created.
myTuple = (0, 1, 2, 3)
# Dictionaries are lists which map a key to a specific value.
myDict = {"One": 1, "Two": 2}

print(myInt)


# Redeclaring works like so, Python has dynamic typing, so the variable type is determined at runtime based on the value of the variable, making redeclaration easy.
myInt = "abc"
print (myInt)

# To access an entry on a list or tuple, use []. 
print(myList[2])
print(myTuple[1])

# Use list slicing to get part of a list. Indexing starts at 1 as 0 is reserved for an empty list or tuple.
print(myList[0:3])
print(myTuple[0:3])
# Step value can also be included to show how many indexes to skip per step. The third number is the step value. Any of these three can be left blank to access the default values.
print(myList[1:4:2])
print(myList[::2]) 
# Negative steps reverse the sequence.
print(myList[::-2])

# Dictionaries are accessed via specified keys. 
print(myDict["One"])

# Variables of different types cannot be combined.
# print("string" + 123)
# Would lead to an error as Python does not allow for two types to be combined in this way. They must be converted into the same variable type for which both can be contained.
print("String " + str(123))

# Global vs local variables in functions
def myFunction():
    myStr = "def"
    print(myStr)
myFunction()
print(myStr)
# Use the global keyword to define a variable by its global value in a function.
def myFunction2():
    global myStr
    print(myStr)
myFunction2()
# The Del keyword deletes a variable. If myStr is printed after deletion, it will give an error.
del myStr
# print(myStr)
