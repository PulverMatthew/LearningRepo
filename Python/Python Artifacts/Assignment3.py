testList = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet"]
#Counts the length of the list.
x = len(testList)
print(x)
#Prints from start index to the third index.
print(testList[:3])
#Prints the 5th index, as the first index is 0.
print(testList[4])
#Appends a new string to the end of the list.
testList.append("Consectetur")
print(testList)
#Inserts a new string to the 0 index of the list, at the beginning.
testList.insert(0, "Adipiscing")
print(testList)
#Sorts list.
testList.sort()
print(testList)
print("\n")

testTuple = ("Lorem", "Ipsum", "Dolor", "Sit", "Amet")
#Counts the length of the list. Uses the same method as lists do with some exceptions.
y = len(testTuple)
print(y)
print("\n")

testDictionary = {
    "Lorem": "Ipsum",
    "Dolor": "Sit",
    "Amet": "Consectetur",
    "Adipscing": "Elit",
    "Sed": "Do"
    }
#Prints out the dictionary.
print(testDictionary)
#Prints the second item out of the dictionary by turning the dict.keys output into a list, and finding the 2nd index.
z = list(testDictionary.keys())[1]
print(z)
#Adds a dictionary entry to the end of the list.
testDictionary.update({"Eiusmod": "Tempor"})
print(testDictionary)
#Deletes a key in the dictionary, then prints.
testDictionary.pop("Lorem")
print(testDictionary)
