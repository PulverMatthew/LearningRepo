#Prints greetings for given name.
def greeter(name):
    print("How are you, " + name)
    print("What's up, " + name)
    print("Hello, " + name)

#Defines names to greet
x = "Matthew"
y = "John"
z = "Doe"
listofNames = [x, y, z]

#Iterates through the list of names.
for x in listofNames:
    greeter(x)
    print("\n")
