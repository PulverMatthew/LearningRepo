# Basic function syntax:
def func1():
    print("I am a function")


# Direct call
func1()
# Called inside print statement, inner function executes, with outer print statement printing nothing as the function has a null return.
print(func1())
# Prints nothing, as function returns nothing.
print(func1)

# Function that takes arguments:
def func2(arg1, arg2):
    print(arg1," ",arg2)

# Function that returns a value
def cube(x):
    return x * x * x

# Testing func2 and cube
func2("Hello", "This")
print(cube(2))

# Function that has default value for an argument. If an argument has an equals sign, the constant it is defined by is the default value.
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# Testing power function
print(power(2,4))
# Should raise to the power of 1, returning 2
print(power(2))

#Function with a variable number of arguments.
def multi_add(*args):
    result = 0 
    for x in args:
        result = result + x 
    return result

#Testing multi_add
print(multi_add(4,5,10,4,10))
