import zipfile
#Tries to extract a file specified in zFile using password variable.
def extractFile(zFile, password):
    #Try to extract zip file using password casted as a byte using utf-8 encoding.
    try:
        zFile.extractall(pwd=bytes(password, 'utf-8'))
        #Return the password if there is no error.
        return password
    except:
        #Return None if it does not work.
        return None
def main():
    #Open HomeworkW8 zip file as zFile variable.
    zFile = zipfile.ZipFile('HomeworkW8.zip')
    #Open the dictionary.txt file to use as a dictionary.
    dictionary = open('dictionary.txt')
    #For every line in the dictionary file, strip the new line characters and use each line as a password to try. 
    for line in dictionary.readlines():
        password = line.strip('\n')
        #Use the string in the given line as a password to try to open zFile zip file.
        guess = extractFile(zFile, password)
        #If the guess is true, print the password and exit successfully.
        if guess:
            print('The password is: ' + password + '\n')
            exit(0)
#If the module being utilized is the main module, run the main function.
if __name__ == '__main__':
    main()
#You've cracked the code!!!Good Job!!!
