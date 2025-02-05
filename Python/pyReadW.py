# Relearning read/write in Python. Did this for my dictionary attack script but helps to relearn.
def main():
    # Opens file, creates if doesn't exist.
    #myFile = open('textfile.txt', 'w+')

    # Appends text to the end of the file. 
    #myFile = open('textfile.txt', 'a')

    # Iterates 'this is some text' 10 times through the file.
    #for x in range(10):
    #    myFile.write('All work no play makes jack a dull boy.\n')
    
    # Closes file when done
    #myFile.close()

    # Open the file back up and read the contents
    #myFile = open('textfile.txt', 'r')

    # If the file is opened in read mode, then...
    #if myFile.mode == 'r':
        #contents = myFile.read()
        #print(contents)
        #fl = myFile.readlines()
        # Prints out the 2nd index of the fl variable, with each line being an index.
        #print(fl[1])
        # Same behavior as lines 10-11, but with different syntax.
        #for x in fl:
        #    print(x)

    # Writes to a specific line by scanning the text file then modifying the line when stored as a variable.
    myFile = open('textfile.txt', 'r')
    data = myFile.readlines()
    data[2] = "Here is a modified line 3\n"
    myFile = open('textfile.txt', 'w')
    myFile.writelines(data)
    myFile.close()

                  
if __name__ == '__main__':
    main()