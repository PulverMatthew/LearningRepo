#List of numbers to add
a = 20
b = 20
c = 30
d = 10
e = 55
f = 601

#Defines the function that adds the numbers together. Prints the inputs and outputs.
def adder(x, y):
    z = x + y
    print("The two numbers being added are:\n")
    print(x)
    print(y)
    print("\nThe total added is: " + str(z) + ".")

# Calls the functions to add 3 pairs of numbers.
adder(a, b)
adder(c, d)
adder(e, f)
