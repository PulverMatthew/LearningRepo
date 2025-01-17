#Does a greeting for a given first and last name.
def fullName(firstName, lastName):
    fullName = firstName + " " + lastName
    print("Hi, " + fullName + ".")

#Dictionary of first and last names.
fullNameList = {
    "John": "Doe",
    "Mike": "Schmidt",
    "William": "Afton",
    }
#Converts keys into a list of first names.
firstNameList = list(fullNameList.keys())
#Converts values into a list of last names
lastNameList = list(fullNameList.values())

#Iterates fullName function throughout the dictionary for the dictionary's length, for this example, it is 3.
for x in range(len(fullNameList)):
    fullName(firstNameList[x], lastNameList[x])


    
